from manage_schedule.models import Schedule
from django.db import models
from django.urls import reverse
from manage_schedule.models import Schedule

class Collection(models.Model):
     
    class Meta:
        verbose_name = ("collection")
        verbose_name_plural = ("collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"pk": self.pk})

    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=31,blank=True)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,blank=True,related_name='collections')


    


