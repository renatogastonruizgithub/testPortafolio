from django.db import models
from Developer.models import Developer
# Create your models here.
class Skill(models.Model):
    nombre=models.TextField()
    imagen=models.ImageField(upload_to='media',null=True) 
    url_skill = models.URLField(max_length=500,blank=True, null=True)
    developer=models.ForeignKey(Developer,on_delete=models.CASCADE)
        
    def __str__(self):
     return (f"{self.nombre}") 