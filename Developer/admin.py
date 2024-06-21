from django.contrib import admin
from django.utils.html import format_html

from utilitis.firebase import upload_image_to_firebase,delete_image_from_firebase
from .models import Developer

# Register your models here. url_developer
@admin.register(Developer)
class AdminDev(admin.ModelAdmin):
    list_display = ('nombre',"apellido","image_preview")
    def save_model(self, request, obj, form, change):
         
        if change and obj.imagen:
            # Si es una modificación, recuperamos el objeto original
            original_obj = self.model.objects.get(pk=obj.pk)
            # Verificamos si la imagen ha cambiado
            
            if original_obj.url_developer:
                delete_image_from_firebase(original_obj.url_developer)
                obj.url_developer = None
                obj.save()
          
                image_data = obj.imagen.read()                
                obj.url_developer = upload_image_to_firebase(image_data, object_id=obj.id)
                obj.save()
        else:         
            if obj.imagen:
                    image_data = obj.imagen.read()  # Leer los datos de la imagen en memoria
                    obj.url_developer = upload_image_to_firebase(image_data, object_id=obj.id)
                    obj.save()
                
        super().save_model(request, obj, form, change)
    
    
    
    def delete_model(self, request, obj):        
        # Elimina la imagen de Cloudinary antes de eliminar la instancia del modelo
        if obj.url_developer:
            delete_image_from_firebase(obj.url_developer)
        super().delete_model(request, obj)
    
    def image_preview(self, obj):
        if obj.url_developer:
            return format_html('<img src="{}" style="width:50px;height:50px;border-radius:50%;object-fit:scale-down">', obj.url_developer)
        else:
            return None

    image_preview.short_description = 'image_preview'