from django.db import models

# Create your models here.
 
class name(models.Model):
    name=models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    
class age(models.Model):
    name=models.ForeignKey(name,on_delete=models.CASCADE)
    age=models.IntegerField()
    
    def __str__(self):
        return self.age

class gender(models.Model):
    gender=models.CharField(max_length=256)
    name=models.ForeignKey(name, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.gender
    