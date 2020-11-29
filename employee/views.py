from django.db.models import Sum, Count
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from employee.forms import EmployeeCreateForm
from django.contrib.auth import logout

from employee.models import User


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = get_user_model().objects.get(email=email)
        except:
            try:
                user = get_user_model().objects.get(username=email)
            except:
                user = None
        if user is not None:
            if user.is_active and user.check_password(password):
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/employee/admin/')
                return HttpResponse(f'Welcome, {user.first_name}')
        return render(request, 'login.html', {'message': 'Invalid Credentials!'})


class AdminDashboard(View):

    def get(self, request):
        if request.user and request.user.is_superuser:
            members = User.objects.filter(is_superuser=False, is_active=True)
            total_members = members.count()
            count_female = members.filter(gender=1).count()
            count_male = members.filter(gender=2).count()
            count_oth = members.filter(gender=3).count()
            return render(request, 'admindashboard.html',
                          {'members': members, 'total_members': total_members, 'count_female': count_female,
                           'count_male': count_male, 'count_oth': count_oth})
        else:
            return HttpResponseForbidden()


class UserDetailView(View):

    def get(self, request, id):
        try:
            member = User.objects.get(id=id)
            return render(request, 'userdetails.html', {'member': member})
        except:
            return Http404


class UserCreateView(View):

    def get(self, request):
        return render(request, 'adduser.html', {'form': EmployeeCreateForm()})

    def post(self, request):
        form = EmployeeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            member.set_password(request.POST.get('password'))
            member.save()
            return HttpResponseRedirect('/employee/admin/')
        else:
            return render(request, 'adduser.html', {'form': form})


def session_logout(request):
    logout(request)
    return HttpResponseRedirect('/employee/login/')
