from django.db import models

# Create your models here.
class ImageOfProject(models.Model):
    imagen = models.ImageField(upload_to='media') 
    url = models.URLField(max_length=500,blank=True, null=True)
    def __str__(self):
        return f"Imagen {self.id}" 
     