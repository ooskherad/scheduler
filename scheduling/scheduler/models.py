from django.db import models
from accounts.models import User


class Scheduler(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.DO_NOTHING, related_name='scheduler')
    title = models.CharField(max_length=25, null=True, blank=True)
    secondary_mobile = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)
    about_you = models.TextField(null=True, default=None)
    sheba_number = models.CharField(max_length=24, null=True, default=True)
    sheba_owner = models.CharField(max_length=25, null=True, default=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    parent = models.ForeignKey(to='self', on_delete=models.DO_NOTHING, null=True, default=None)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class SchedulerServices(models.Model):
    scheduler = models.ForeignKey(to=Scheduler, on_delete=models.DO_NOTHING, related_name='services')
    service = models.ForeignKey(to=Services, on_delete=models.DO_NOTHING)
    about_your_service = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, default=None)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
