from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


class ExtractForm(forms.Form):
    extract = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%'}))

class ExtractUrlForm(forms.Form):
    urla = forms.URLField()
    urla.widget.attrs['class'] = 'form-control'

class ExtractText(forms.Form):
    urlb = forms.CharField()
    urlb.widget.attrs['class'] = 'form-control'


class UploadFileForm(forms.Form):
    client = forms.CharField(max_length=50)
    date_crawled = forms.DateField(widget=forms.widgets.DateInput())
    file = forms.FileField()

