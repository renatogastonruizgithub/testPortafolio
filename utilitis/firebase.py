import firebase_admin
from firebase_admin import credentials, storage
import io
from datetime import datetime
from PIL import Image
# Inicializar la aplicación de Firebase
cred = credentials.Certificate("./utilitis/key.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'portafolio-ecd13.appspot.com'
})

def generar_id():
        now = datetime.now()
        return f"{now.minute}{now.second}{now.microsecond}"
    
    
def upload_image_to_firebase(image_data, object_id):
    try:
    
        # Convertir los datos de la imagen en un objeto de imagen de PIL
        image_pil = Image.open(io.BytesIO(image_data))

        # Verificar si la imagen original está en formato PNG
        if image_pil.format == 'PNG':
            # Crear un búfer de memoria para almacenar la imagen en formato PNG
            image_buffer = io.BytesIO()
            image_pil.save(image_buffer, format='PNG')

            # Obtener una referencia al bucket de almacenamiento de Firebase
            bucket = storage.bucket()

            # Crear una referencia al archivo en Firebase Storage con un nombre único
            filename = f"portafolio/{str(object_id)}_{generar_id()}.png"
            blob = bucket.blob(filename)

            # Subir los datos de la imagen al archivo en Firebase Storage
            blob.upload_from_string(image_buffer.getvalue(), content_type='image/png')

            # Obtener la URL pública del archivo cargado          
            blob.make_public()

    # Devuelve la URL de descarga pública del archivo
            return blob.public_url
            
        else:
            # Convertir la imagen a modo RGB si está en modo LA o P
            if image_pil.mode == 'LA':
                image_pil = image_pil.convert('RGB')
            elif image_pil.mode == 'P':
                image_pil = image_pil.convert('RGB')

            # Crear un búfer de memoria para almacenar la imagen en formato JPEG
            image_buffer = io.BytesIO()
            image_pil.save(image_buffer, format='JPEG')

            # Obtener una referencia al bucket de almacenamiento de Firebase
            bucket = storage.bucket()

            # Crear una referencia al archivo en Firebase Storage con un nombre único
            filename = f"portafolio/{str(object_id)}_{generar_id()}.jpeg"
            blob = bucket.blob(filename)

            # Subir los datos de la imagen al archivo en Firebase Storage
            blob.upload_from_string(image_buffer.getvalue(), content_type='image/jpeg')

            # Obtener la URL pública del archivo cargado
            blob.make_public()

                # Devuelve la URL de descarga pública del archivo
            return blob.public_url

    except Exception as e:
        print("Error:", e)
        return None


def delete_image_from_firebase(url): 
    try:    

        # Extraer el nombre del archivo de la URL
        filename = url.split('/')[-1].split('portafolio/')[0]
        print("filename ", filename)       
        
        # Obtener una referencia al bucket de almacenamiento de Firebase
        bucket = storage.bucket()

        # Obtener una referencia al archivo en Firebase Storage
        blob = bucket.blob("portafolio/"+filename)
        print("referencia ", blob)
        # Eliminar el archivo
        blob.delete()       
        return True  # Éxito al eliminar el archivo

    except Exception as e:
        print("Error al eliminar el archivo:", e)
        return False  # Error al eliminar el archivo
    
