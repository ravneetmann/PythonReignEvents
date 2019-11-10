from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm


def list_event(request):
    event = Event.objects.all()
    return render(request, 'event.html', {'event': event})


def create_event(request):
    form = EventForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_event')

    return render(request, 'event-form.html', {'form': form})


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





