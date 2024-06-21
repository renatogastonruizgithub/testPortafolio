
from django.utils.html import format_html

        
def add_image_preview(admin_class):
    #metodo para agregar el imagen preview
    def image_preview(self, obj):
        if obj.cloudinary_url:
            return format_html('<img src="{}" style="width:50px;height:50px;border-radius:50%;object-fit:scale-down">', obj.cloudinary_url)
        else:
            return None

    image_preview.short_description = 'image_preview'
    admin_class.image_preview = image_preview

#funciones para subir imagenes en admin



