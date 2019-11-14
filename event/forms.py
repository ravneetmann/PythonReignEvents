from django.shortcuts import forms
from .models import Event
from django.contrib.auth import (authenticate, get_user_model)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event

    fields = ['quantity', 'description', 'price']

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
            return super(UserLoginForm, self).clean(*args, **kwargs)

    class UserRegisterForm(forms.ModelForm):
            email = forms.EmailField(label='Email Address')
            email2 = forms.EmailField(label='Confirm Email')
            password = forms.CharField(widget=forms.PasswordInput)

            def clean(self, *args, **kwargs):
                email2 = self.cleaned_data.get('email')

            class Meta:
                model = User
                fields = [
                    'username',
                    'email',
                    'email2',
                    'passowrd'
                ]
            def clean_email(self):
                email = self.cleaned_data.get('email')
                email2=self.cleaned_data.get('email2')
                if email != email2:
                    raise forms.ValidationError("Sorry, your emails are not matching!")
                email_qs = User.objects.filter(email=email)
                if email_qs.exists():
                    raise forms.ValidationError("This email is already associated with another account. Please enter another valid email")
                return email







