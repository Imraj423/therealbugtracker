from django.urls import reverse
from django.db import models
from django.utils import timezone
from custom_user.models import CustomUser


class Ticket(models.Model):
    New = 'NEW'
    In_Progress = 'IN PROGRESS'
    Done = 'DONE'
    Invalid = 'INVALID'
    STATUS_CHOICES = [(New, 'New'), (In_Progress, 'In Progress'),
        (Done, 'Done'), (
        Invalid, 'Invalid')]
    
    status = models.CharField(
        default=New, choices=STATUS_CHOICES, max_length=15)
    user_assigned = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="user_assigned", null=True, blank=True)
    completed_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="completed_by", null=True, blank=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name="created_by", null=True, blank=True)
    title = models.CharField("Title", max_length=30)
    time_filled = models.DateTimeField(default=timezone.now)
    description = models.CharField("Description", max_length=100)

    def __str__(self):
        return self.title
