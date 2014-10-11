from datetime import datetime
from django.shortcuts import render
from sha_events.models import EventForm, Event, HashTag
from django.shortcuts import redirect


class NewEventErrorCode:
    DATE = 1
    LOCATION = 2
    NAME = 3
    SQL = 4


def events_from_range(request, north, south, east, west):
    events_nearby = Event.objects.filter(latitude__gte=south, latitude__lte=north, longitude__gte=west, longitude__lte=east);
    return render(request, 'sha_events/events_from_range.html', {'events': events_nearby})


def create_hash_tags(hash_str):
    hashes = []
    for single_hash in hash_str.split(','):
        single_hash = single_hash.strip()
        if single_hash:
            new_hash, created = HashTag.objects.get_or_create(name=single_hash)
            hashes.append(new_hash.id)

    return hashes


def convert_date(bad_formated):
    return datetime.strptime(
        bad_formated, '%d/%m/%Y %H:%M').strftime('%Y-%m-%d %H:%M')


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
        evt = Event.objects.create(start_date=start_date, stop_date=stop_date, max_count=max_count, latitude=latitude,
                                   longitude=longitude, name=event_name, creator_id=request.user.id, description=request.POST['description'])
        evt.hash_tags = create_hash_tags(request.POST['hashtags'])
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
                  {"form": EventForm(), 'add_error': add_error, 'autocomplete_hashes': HashTag.objects.all()})