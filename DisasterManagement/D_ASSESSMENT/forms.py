from django import forms
from .models import *

class DisasterReportForm(forms.ModelForm):
	class Meta:
		model = Disaster 
		fields = ['disaster_type', 'alert']


