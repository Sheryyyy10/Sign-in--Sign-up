from django import forms

class Indexxforms(forms.Form):
    Email= forms.EmailField()
    Password= forms.CharField()
