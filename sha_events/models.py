from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, NumberInput
from django.utils.translation import gettext as _


class HashTag(models.Model):
    name = models.CharField(max_length=30)


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField()
    description = models.TextField()
    creator = models.ForeignKey(User)
    max_count = models.IntegerField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    hash_tags = models.ManyToManyField(HashTag)


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'max_count', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'type': ''}),
            'max_count': NumberInput(attrs={'value': '5', 'style': 'height:34px', 'min': '0'})
        }
        error_messages = {
            'name': {
                'max_length': _("This name is too long."),
            },
        }
        labels = {
            'name': _('Event name'),
            'max_count': _('Max number of attendants (zero means infinity)')
        }


