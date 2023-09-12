from django.forms import ModelForm
from .models import Products, Stock, Invoice

class InvocieForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'