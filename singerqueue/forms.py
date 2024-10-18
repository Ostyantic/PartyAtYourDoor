from django import forms
from .models import Singer


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = "__all__"


