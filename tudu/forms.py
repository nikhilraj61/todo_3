
from django import forms
from .models import Tudus

class TuduForm(forms.ModelForm):
    
	class Meta:
		model = Tudus
		fields = '__all__'