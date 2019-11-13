from django import forms

class MainForm(forms.Form):
    CurrentStation = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'id' : 'CurrentStation',
        'class': 'ui-autocomplete-input rounded-0 ui-autocomplete-loading form-control form-control-lg mb-3 col-sm-12 text-center',
        'autocomplete':'off',

    }))
    DropStation = forms.CharField(label='أكتب المحطة اللي عايز تروحلها',max_length=100,widget=forms.TextInput(attrs={
        'id':'DropStation',
        'class': 'ui-autocomplete-input rounded-0 ui-autocomplete-loading form-control form-control-lg mb-3 col-sm-12 text-center',
        'autocomplete':'off'
    }))
