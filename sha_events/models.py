from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, NumberInput, Textarea
from django.utils.translation import gettext as _


class HashTag(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    stop_date = models.DateTimeField(null=True)
    description = models.TextField()
    creator = models.ForeignKey(User)
    max_count = models.IntegerField()
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    human_readable_location = models.CharField(max_length=200, default='')
    hash_tags = models.ManyToManyField(HashTag)
    participants = models.ManyToManyField(User, related_name='participants')


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'max_count', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'type': '', 'style': 'width:225px'}),
            'max_count': NumberInput(attrs={'value': '5', 'style': 'height:34px', 'min': '0'}),
            'description': Textarea(attrs={'rows': 5, 'style': 'width:225px'})
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


