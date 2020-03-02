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


# class Finito(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = [
#             "status"
#         ]


class NewTicket(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100, widget=forms.Textarea)



# class EditTicket(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = [
#             "title",
#             "description"
#         ]


# form = EditTicket()

# # Creating a form to change an existing article.
# ticket = Ticket.objects.get('title')
# form = EditTicket(instance=ticket)
