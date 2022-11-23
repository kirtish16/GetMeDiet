from django import forms
from .models import Breakfast , Lunch , Dinner

class BreakfastForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = "__all__"

class LunchForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = "__all__"

class DinnerForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = "__all__"
