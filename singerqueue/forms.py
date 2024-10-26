from django import forms
from .models import Singer, ContactInfo


class SingerForm(forms.ModelForm):
    class Meta:
        model = Singer
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = "__all__"
        widgets = {
            'social_types': forms.Select(attrs={
                'class': 'text-white text-center bg-p4 border-2 border-black focus:border-black focus:ring-black text-sm block w-full p-2.5'
            }),
        }