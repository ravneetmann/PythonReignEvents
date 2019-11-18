from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_event, create_event, update_event, delete_event, index_page, registration_choice,\
    signup, redirect_to_home, list_employees, choose_date, list_available_employees, assign_employee, remove_employee

urlpatterns = [
    path('', index_page, name='login_page'),
    path('registration-choice', registration_choice, name='registration_choice'),
    path('signup', signup, name='signup'),
    path('list_event', list_event, name='list_event'),
    path('list_employees', list_employees, name='list_employees'),
    path('new', create_event, name='create_event'),
    path('update/<int:id>/', update_event, name='update_event'),
    path('delete/<int:id>/', delete_event, name='delete_event'),
    # path('login_page', login_page, name='login_page')
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home', redirect_to_home, name='redirect_to_home'),
    path('choose_date', choose_date, name='choose_date'),
    path('list_available_employees/<int:event_id>', list_available_employees, name='list_available_employees'),
    path('assign_employee/<int:event_id>/<int:employee_id>', assign_employee, name='assign_employee'),
    path('remove_employee/<int:event_id>/<int:employee_id>', remove_employee, name='remove_employee')

]


#CRUD - CREATE, READ, UPDATE, DELETE