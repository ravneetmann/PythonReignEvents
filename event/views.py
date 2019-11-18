from django.shortcuts import render, redirect
from .models import Event, BaseUser
from .forms import EventForm, RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def index_page(request):
    return render(request, 'index.html')


@login_required()
def redirect_to_home(request):
    return render(request, 'logged-in-home.html')


def registration_choice(request):
    return render(request, 'registration-choice.html')


# @login_required
def list_event(request):
    event = Event.objects.all()
    return render(request, 'event.html', {'event': event})


def list_employees(request):
    employee = BaseUser.objects.filter(is_employee=True)
    return render(request, 'employees.html', {'employee': employee})


def choose_date(request):
    event = Event.objects.all()
    return render(request, 'choose-date.html', {'event': event})


def list_available_employees(request, event_id):
    all_employee = BaseUser.objects.filter(is_employee=True)
    event = Event.objects.get(id=event_id)
    employee_working_event = event.employee_assigned.all()

    all_employee_set = set(all_employee)
    employee_working_event_set = set(employee_working_event)
    available_employee = all_employee_set - employee_working_event_set
    available_employee = list(available_employee)

    return render(request, 'list-available-employees.html', {'employee_working_event': employee_working_event,
                                                             'available_employee': available_employee,
                                                             'event': event})


def assign_employee(request, event_id, employee_id):
    event = Event.objects.get(id=event_id)
    employee = BaseUser.objects.get(id=employee_id)
    event.employee_assigned.add(employee)
    event.save()
    return render(request, 'assignment-confirmation.html', {'employee': employee, 'event': event})


def remove_employee(request, event_id, employee_id):
    event = Event.objects.get(id=event_id)
    employee = BaseUser.objects.get(id=employee_id)
    event.employee_assigned.remove(employee)
    event.save()
    return render(request, 'removal-confirmation.html', {'employee': employee, 'event': event})


def create_event(request):
    form = EventForm(request.POST or None)

    if form.is_valid():
        form.save()
        return render(request, 'event-confirmation.html', {'event': form})

    return render(request, 'event-form.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('redirect_to_home')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('list_event')

    return render(request, 'event-form.html', {'form': form, 'event': event})


def delete_event(request, id):
    event = Event.objects.get(id=id)

    if request.method == 'POST':
        event.delete()
        return redirect('list_event')

    return render(request, 'event-delete-confirm.html', {'event': event})





