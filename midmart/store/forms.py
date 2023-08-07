from django.forms import ModelForm
from .models import *
class productform(ModelForm):
    class Meta:
        model = product
        fields = '__all__'