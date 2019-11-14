from django.shortcuts import render, redirect

from django.contrib.auth import (authenticate, get_user_model, login, logout)

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned.data.get('username')
        password = form.cleaned.data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form
    }
    return render (request, "2login.html", context)


def list_event(request):
    event = Event.objects.all()
    return render(request, 'event.html', {'event': event})


def create_event(request):
    form = forms.EventForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_event')

    return render(request, 'event-form.html', {'form': form})


def update_event(request, id):
    event = Event.objects.get(id=id)
    form = forms.EventForm(request.POST or None, instance=event)

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





