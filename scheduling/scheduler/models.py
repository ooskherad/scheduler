from django.db import models
from accounts.models import User


class Scheduler(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='scheduler')
    title = models.CharField(max_length=25, null=True, blank=True)
    secondary_mobile = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    about_you = models.TextField(null=True, default=None)
    sheba_number = models.CharField(max_length=24, null=True, default=True)
    sheba_owner = models.CharField(max_length=25, null=True, default=True)

    # objects =

    def __str__(self):
        return self.title
