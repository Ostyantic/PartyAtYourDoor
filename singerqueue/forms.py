from django import forms
from .models import Singer, ContactInfo
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


def validate_room_id(value):
    try:
        superuser = User.objects.get(is_superuser=True)
        if value.lower() != superuser.room_id.lower():
            raise ValidationError("Incorrect Room ID. Please try again.")
    except User.DoesNotExist:
        raise ValidationError("Room does not exist.")


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
            'room_id': forms.TextInput(attrs={
                'class': 'text-white text-center text-2xl placeholder-white placeholder:text-center placeholder:text-xl bg-p4 border-2 border-black focus:placeholder-opacity-0 focus:border-black focus:ring-black block w-full'
            })
        }

    room_id = forms.CharField(max_length=6, validators=[validate_room_id])

    def clean_room_id(self):
        return self.cleaned_data["room_id"]
