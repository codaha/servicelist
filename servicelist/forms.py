from django import forms
from .models import *

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = []
    