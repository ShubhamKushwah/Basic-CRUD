from django import forms
from .models import Programmer


class ProgForm(forms.ModelForm):

    class Meta:
        model = Programmer
        fields = [
            'username',
            'phone_no'
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = Programmer.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username already registered!")
        return username

    def clean_phone_no(self):

        phone = self.cleaned_data.get("phone_no")

        if not phone.isdigit():
            raise forms.ValidationError("It contains unexpected characters")
        return phone.strip()
