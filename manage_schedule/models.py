from django.db import models
from django.urls import reverse

class Schedule(models.Model):
    class Meta:
        verbose_name = ("schedule")
        verbose_name_plural = ("schedules")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})

    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    






