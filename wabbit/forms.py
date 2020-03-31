from django import forms
from .models import Ticket

# from django.contrib.auth.models import User


class EditTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "title",
            "description",
            "status",
            "time_filled"

        ]




class NewTicket(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100, widget=forms.Textarea)



