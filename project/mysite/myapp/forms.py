from django import forms  
from .models import Input, STATION

class InputForm(forms.ModelForm):  

    attrs = {'class ' : 'form−control ',
             'onchange ' : 'this.form.submit() '}

    station = forms.ChoiceField(choices=STATION, required=True,
                              widget=forms.Select(attrs = attrs))
    class Meta:

        model = Input
        fields = ['station']
