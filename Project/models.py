from django.db import models
from Developer.models import Developer 

# Create your models here.
class Project(models.Model):
    nombre=models.TextField()
    imagen=models.ImageField(upload_to='media',null=True) 
    url_portada = models.URLField(max_length=500,blank=True, null=True)
    url_proyecto=models.URLField(blank=True, null=True)
    descripcionPortada=models.TextField()
    detalles=models.TextField()
    skills=models.ManyToManyField('Skill.Skill') 
    imagenesSlider = models.ManyToManyField('ImagesOfProject.ImageOfProject')
    developer=models.ForeignKey(Developer,on_delete=models.CASCADE)
    
    def __str__(self):
     return (f"Proyecto {self.nombre}")
 
  
