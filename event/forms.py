from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Event, BaseUser

User = get_user_model()


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description', 'budget', 'date', 'location']
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class RegistrationForm(UserCreationForm):
    is_employee = forms.BooleanField(required=False)
    is_customer = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_employee', 'is_customer']


class ChangeRegistrationForm(UserChangeForm):
    is_employee = forms.BooleanField(required=False)
    is_customer = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'is_employee', 'is_customer']


class LoginForm(AuthenticationForm):
    class Meta:
        model = BaseUser
        fields = ['username', 'password']
#
#
# class EmployeeRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeUser
#         fields = ['identifier', 'email', 'first_name', 'last_name']
