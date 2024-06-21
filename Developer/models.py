from django.db import models
from datetime import date
# Create your models here.

class Developer(models.Model):
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    descripcion=models.TextField(blank=True)
    ciudad=models.CharField(max_length=200)
    fechaNacimiento= models.DateField()
    imagen=models.ImageField(upload_to='media',null=True) 
    url_developer = models.URLField(max_length=500,blank=True, null=True)
    
    def fechaFormat(self):
        return self.fechaNacimiento.strftime('%d %b %Y')
    
    def edad(self):
        today = date.today()
        edad = today.year - self.fechaNacimiento.year - ((today.month, today.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))
        return (f"{edad} años")
    
    def __str__(self):
     return (f"Desarrollador {self.nombre} {self.apellido}") 
 
 
class DeveloperDetail:
    def __init__(self, developer, certificated, skill, project):
        self.nombre = developer.nombre
        self.apellido = developer.apellido
        self.descripcion = developer.descripcion
        self.ciudad = developer.ciudad
        self.fechaNacimiento = developer.fechaNacimiento
        self.certificated = certificated
        self.skill = skill
        self.project = project
         