from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


# User = get_user_model()


class Event(models.Model):
    description = models.CharField(max_length=100)
    location_choices = [
        ('Downtown Montreal', 'Downtown Montreal'),
        ('Laval', 'Laval'),
        ('West Island', 'West Island'),
        ('South Shore', 'South Shore'),
    ]
    location = models.CharField(choices=location_choices, default='Downtown Montreal', max_length=30)
    budget = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField()
    employee_assigned = models.ManyToManyField('BaseUser')

    def __str__(self):
        return self.description


class BaseUser(AbstractUser):
    username = models.CharField(unique=True, max_length=30)
    # email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    is_employee = models.BooleanField('employee status', default=True)
    is_customer = models.BooleanField('customer status', default=False)

    def clean(self):
        if (self.is_employee is True) and (self.is_customer is True):
            raise ValidationError('An account cannot be both employee and customer. Choose one')
        elif (self.is_employee is False) and (self.is_customer is False):
            raise ValidationError('An account has to be either an employee or a customer. Choose one')


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     identifier = models.CharField(max_length=40, unique=True)
#     USERNAME_FIELD = 'identifier'
#     REQUIRED_FIELDS = ['username', 'password1', 'password2']
#     is_employee = models.BooleanField('employee status')
#     is_customer = models.BooleanField('customer status')






# class EmployeeUser(models.Model):
#     user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
#     is_employee = models.BooleanField('employee status', default=True)
#     is_customer = models.BooleanField('customer status', default=False)
#
#     def __str__(self):
#         return str('EMPLOYEE -- username: ' + self.user.identifier + ' email: ' + self.user.email + ' name '
#                    + self.user.first_name + ' ' + self.user.last_name)
#
#
# class CustomerUser(models.Model):
#     user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
#     is_employee = models.BooleanField('employee status', default=False)
#     is_customer = models.BooleanField('customer status', default=True)
#
#     def __str__(self):
#         return str('CUSTOMER -- username: ' + self.user.identifier + ' email: ' + self.user.email + ' name '
#                    + self.user.first_name + ' ' + self.user.last_name)

