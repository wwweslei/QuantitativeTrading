from django import forms

from .models import Portfolio


class DateInput(forms.DateInput):
    input_type = 'date'


class PortfolioForm(forms.ModelForm):
    
    class Meta:
        model = Portfolio
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }