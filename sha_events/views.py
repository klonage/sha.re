from django.shortcuts import render
from sha_events.models import EventForm


def new_event(request):
    return render(request, "sha_events/add_event.html", {"form": EventForm()})