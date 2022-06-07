from django.db import models

# Create your models here.
 
class info(models.Model):
    name=models.CharField(max_length=256,unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=256)
    def __str__(self):
        return self.name

        