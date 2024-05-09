#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pillow-avif-plugin


# In[ ]:


pip install py7zr


# In[ ]:


from PIL import Image
import pillow_avif
import zipfile
import py7zr
import os


# ### Convertir las imágenes de AVIF a PNG o JPG

# In[ ]:


# Pide que el usuario asigne un nombre a la carpeta
folder_name = input("Ingrese el nombre de la carpeta: ")

# Definir las carpetas
input_folder = 'C:\\Users\\juant\\Desktop'  # Cambiar esto a la carpeta en donde están guardadas las imágenes AVIF
output_folder = os.path.join('C:\\Users\\juant\\Desktop', folder_name)  # Cambiar esto a la carpeta en donde se desea guardar

# Selección de formato
while True:
    print("¿A qué tipo de archivo lo convertimos?:")
    print("1. PNG")
    print("2. JPG")
    
    # Solicitar al usuario que elija el formato de salida
    format_choice = input("Ingrese el número de la opción correspondiente: ").strip()

    if format_choice == '1':
        output_format = 'PNG'
        output_ext = 'png'
        break  # Salir del bucle si la elección es válida

    elif format_choice == '2':
        output_format = 'JPEG'
        output_ext = 'jpg'
        break  # Salir del bucle si la elección es válida
    
    else:
        print("Selección no válida. Inténtelo de nuevo.")

# Crear la carpeta en caso no exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print(f'La carpeta "{output_folder}" ya existe.')

# Listar todos los archivos AVIF en la carpeta de inicio
avif_files = [f for f in os.listdir(input_folder) if f.endswith('.avif')]

# Iterar entre los archivos AVIF y convertirlas a PNG
for avif_file in avif_files:
    avif_path = os.path.join(input_folder, avif_file)
    output_file = avif_file.replace('.avif', f'.{output_ext}')
    output_path = os.path.join(output_folder, output_file)

    # Guardar la imagen en la carpeta de destino
    with Image.open(avif_path) as img:
        img.save(output_path, output_format)

    # Mensaje que indica qué imágenes se convirtieron
    print(f'Se convirtió {avif_file} a {os.path.basename(output_path)}')

# Mensaje que confirma que todas las imágenes se convirtieron con éxito
print('La conversión se ha realizado con éxito.')


# ### Convertir la carpeta finalizada en un archivo ZIP o RAR

# In[ ]:


while True:
    print("¿En qué formato lo comprimimos?:")
    print("1. ZIP")
    print("2. RAR")
    format_choice = input("Seleccione el formato de salida: ").strip()

    if format_choice == '1':
        # Retiene el nombre de la carpeta inicial y hace que el ZIP se guarde en la misma ubicación
        folder_to_zip = output_folder
        output_zip_file = f'{output_folder}.zip'

        # Crea un archivo ZIP y agrega los archivos de la carpeta
        with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(folder_to_zip):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, folder_to_zip)
                    zipf.write(filepath, arcname)
                    
        # Mensaje que confirma que todas las imágenes se convirtieron con éxito
        print("La compresión a ZIP se realizó con éxito")
        break  # Salir del bucle si la elección es válida

    elif format_choice == '2':
        # Retiene el nombre de la carpeta inicial y hace que el RAR se guarde en la misma ubicación
        folder_to_rar = output_folder
        output_rar_folder = f'{output_folder}.rar'

        # Crea un archivo ZIP y agrega los archivos de la carpeta
        with py7zr.SevenZipFile(output_rar_folder, 'w') as rarfile:
            for foldername, subfolders, filenames in os.walk(folder_to_rar):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, folder_to_rar)
                    rarfile.write(filepath, arcname)

        # Mensaje que confirma que todas las imágenes se convirtieron con éxito
        print('La compresión a RAR se ha realizado con éxito.')
        break  # Salir del bucle si la elección es válida

    else:
        print("Selección no válida. Inténtelo de nuevo.")

