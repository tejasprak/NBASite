from django import forms
from functools import partial
from django.contrib.admin import widgets

class tform(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()

class pform(forms.Form):
    asd = forms.CharField()
