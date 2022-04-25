
from django import forms
from django.forms import ModelForm, fields
from django.forms.widgets import NumberInput
from .models import DailyPlan



class DailyPlanForm(ModelForm):

    class Meta:
        model = DailyPlan
        fields = ['task', 'description', 'task_complete', 'deadline_day', 'deadline_time']

        labels = {'task':'Plan','deadline_time':'Deadline-Time(hour:min:am/pm)' }
        
        widgets = {
            'description': forms.Textarea(attrs={'cols': 3}),
            'deadline_day': forms.NumberInput(attrs={'type':'date'}),
            'deadline_time': forms.TimeInput(attrs={'type': 'time'})
           
            
            }
       

