from django import forms
from django.forms import ModelForm
from .models import Thread, ThreadMessage

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['threadTitle', 'threadDesc', 'threadImg']

class ThreadMessageForm(ModelForm):
    class Meta:
        model = ThreadMessage
        fields = ['textMessage']
