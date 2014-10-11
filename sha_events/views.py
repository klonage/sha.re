from datetime import datetime
from django.shortcuts import render
from sha_events.models import EventForm, Event
from django.shortcuts import redirect


class NewEventErrorCode:
    DATE = 1
    LOCATION = 2
    NAME = 3
    SQL = 4


def convert_date(bad_formated):
    return datetime.strptime(
        bad_formated, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')


def save_new_event(request):
    try:
        start_date = convert_date(request.POST['start-date'])
        stop_date = convert_date(request.POST['stop-date'])
    except ValueError:
        return NewEventErrorCode.DATE

    max_count = int(request.POST['max_count'])

    event_name = request.POST['name']
    if len(event_name) < 5:
        return NewEventErrorCode.NAME

    try:
        latitude = float(request.POST['latitude'])
        longitude = float(request.POST['longitude'])
    except ValueError:
        return NewEventErrorCode.LOCATION

    # noinspection PyBroadException
    try:
        Event.objects.create(start_date=start_date, stop_date=stop_date, max_count=max_count, latitude=latitude,
                             longitude=longitude, name=event_name, creator_id=request.user.id)
    except:
        return NewEventErrorCode.SQL
    else:
        return 0


def just_added_event(request):
    return render(request, 'sha_events/just_added_event.html');


def new_event(request):
    add_error = 0
    if request.method == 'POST':
        add_error = save_new_event(request)
        if add_error == 0:
            return redirect('/event/added')
    return render(request, "sha_events/add_event.html",
                  {"form": EventForm(), 'add_error': add_error})