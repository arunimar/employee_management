from django.forms import ModelForm, fields

from employee.models import User


class EmployeeCreateForm(ModelForm):
    image = fields.ImageField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'password', 'address', 'phone', 'username', 'image']

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
