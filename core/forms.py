from django import forms

from core.models import PortifolioUser, type_choices


class PortifolioUserForm(forms.Form):
    class Meta:
        model = PortifolioUser

    type = forms.ChoiceField(choices=type_choices, required=True)
    cod = forms.CharField(max_length=10, required=True)
    quantity = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    date = forms.DateField(
        required=True, widget=forms.TextInput(attrs={"type": "date"})
    )
