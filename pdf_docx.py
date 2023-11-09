from pdf2docx import Converter

# Solicitar al usuario la ruta del archivo PDF de entrada
pdf_file = input("Ingrese la ruta del archivo PDF de entrada: ")

# Verificar si el archivo PDF existe
import os
if not os.path.exists(pdf_file):
    print("El archivo PDF especificado no existe.")
else:
    # Solicitar al usuario el nombre del archivo DOCX de salida
    docx_name = input("Ingrese el nombre del archivo DOCX de salida (sin extensión .docx): ")

    # Obtener la ruta del directorio del archivo PDF
    pdf_dir = os.path.dirname(pdf_file)

    # Generar la ruta completa del archivo DOCX de salida en el mismo directorio
    docx_file = os.path.join(pdf_dir, docx_name + ".docx")

    # Realiza la conversión de PDF a DOCX
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

    print(f"Se ha convertido {pdf_file} a {docx_file}")