from django.contrib import admin
from django.urls import path, include
from employee.views import LoginView, AdminDashboard, UserDetailView, UserCreateView, session_logout

app_name = 'employee'

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', session_logout, name='logout'),
    path('admin/', AdminDashboard.as_view()),
    path('admin/user/view/<int:id>', UserDetailView.as_view(), name='user_detail'),
    path('admin/user/create/', UserCreateView.as_view(), name='create_user'),
]
