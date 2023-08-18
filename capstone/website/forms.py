from django.forms import ModelForm
from .models import Endorser

class EndorserForm(ModelForm):
    class Meta:
        model = Endorser
        fields = '__all__'