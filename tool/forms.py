from django import forms

class ExtractForm(forms.Form):
    extract = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%'}))

class ExtractUrlForm(forms.Form):
    urla = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))