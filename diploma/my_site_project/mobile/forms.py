from django.forms import ModelForm
from .models import Mobile


class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = ['name', 'email', 'username']
