from django import forms
from django.forms import ModelForm
from .models import *

# create the form for all data model
class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields='__all__'