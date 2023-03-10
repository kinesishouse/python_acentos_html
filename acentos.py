import re
from bs4 import BeautifulSoup

# Abrir el archivo HTML
with open("acv.html", "r") as f:
    contenido_html = f.read()

# Crear un objeto BeautifulSoup
soup = BeautifulSoup(contenido_html, "html.parser")

# Lista de etiquetas en las que queremos hacer el cambio selectivo
etiquetas_seleccionadas = ["p", "h1", "h2"]

# Iterar sobre todas las etiquetas seleccionadas
for etiqueta in soup.find_all(etiquetas_seleccionadas):
    # Convertir las palabras acentuadas a sus entidades HTML correspondientes
    contenido_sin_acentos = etiqueta.text
    contenido_sin_acentos = re.sub('[áéíóúÁÉÍÓÚñ]', lambda x: {'á': '&aacute;', 'é': '&eacute;', 'í': '&iacute;', 'ó': '&oacute;', 'ú': '&uacute;', 'Á': '&Aacute;', 'É': '&Eacute;', 'Í': '&Iacute;', 'Ó': '&Oacute;', 'Ú': '&Uacute;', 'ñ': '&ntilde;'}[x.group()], contenido_sin_acentos)

    # Reemplazar el contenido de la etiqueta con el contenido sin acentos
    etiqueta.string = contenido_sin_acentos

# Guardar el nuevo archivo HTML
with open("archivo_sin_acentos.html", "w") as f:
    f.write(str(soup.prettify(formatter=None)))
