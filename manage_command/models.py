from django.db import models
from django.urls import reverse
from manage_collection.models import Collection

class Command(models.Model):
    class Meta:
        verbose_name = ("command")
        verbose_name_plural = ("commands")

    def __str__(self):
        return self.command

    def get_absolute_url(self):
        return reverse("commands_detail", kwargs={"pk": self.pk})

    id = models.AutoField(primary_key=True,unique=True)
    command = models.CharField(max_length=50,blank=True)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE,related_name='commands')





