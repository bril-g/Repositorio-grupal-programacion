class Archivo: 

	def __init__(self, nombre: str, tamano_bytes: int): 
		self.nombre = nombre 
		self.tamano_bytes = tamano_bytes 

class Directorio: 

	def __init__(self, nombre: str): 
		self.nombre = nombre 
		self.archivos = [] # Lista de objetos de tipo Archivo 
		self.subdirectorios = [] # Lista de objetos de tipo Directorio 
		
def calcular_tamano_total(directorio: Directorio) -> int:
	total = 0
	for archivo in directorio.archivos:
		total += archivo.tamano_bytes

	for subdirectorio in directorio.subdirectorios:
		total += calcular_tamano_total(subdirectorio)

	return total

def buscar_por_extension(directorio: Directorio, extension: str, ruta_padre: str = "") -> list[str]:
    if ruta_padre == "":
        ruta_actual = directorio.nombre
    else:
        ruta_actual = f"{ruta_padre}/{directorio.nombre}"

    resultados = []

    for archivo in directorio.archivos:
        if archivo.nombre[-len(extension):] == extension:
            resultados.append(f"{ruta_actual}/{archivo.nombre}")

    for subdirectorio in directorio.subdirectorios:

        resultados += buscar_por_extension(subdirectorio, extension, ruta_actual)

    return resultados

def limpiar_archivos_vacios(directorio: Directorio) -> int:
    eliminados = 0

    for archivo in list(directorio.archivos):
        if archivo.tamano_bytes == 0:
            directorio.archivos.remove(archivo)
            eliminados += 1

    for subdirectorio in directorio.subdirectorios:
        eliminados += limpiar_archivos_vacios(subdirectorio)

    return eliminados

# Directorios
root = Directorio("root")
imagenes = Directorio("imagenes")
proyectos = Directorio("proyectos")
temp = Directorio("temp")

# Archivos
arch1 = Archivo("documento.pdf", 1500)
arch2 = Archivo("config.txt", 0)
arch3 = Archivo("foto1.png", 2000)
arch4 = Archivo("foto2.png", 3500)
arch5 = Archivo("avance.pdf", 800)
arch6 = Archivo("log.txt", 0)

# Root
root.archivos.append(arch1)
root.archivos.append(arch2)
root.subdirectorios.append(imagenes)
root.subdirectorios.append(proyectos)

# Imagenes
imagenes.archivos.append(arch3)
imagenes.archivos.append(arch4)

# Proyectos
proyectos.archivos.append(arch5)
proyectos.subdirectorios.append(temp)

# Temp
temp.archivos.append(arch6)

# --- Prueba funciones ---
# A) Tamaño total
tamano_total = calcular_tamano_total(root)
print(f"Tamaño total del sistema: {tamano_total} bytes")

# B) Búsqueda por extensión
pdfs_encontrados = buscar_por_extension(root, ".pdf")
print(f"Archivos PDF encontrados: {pdfs_encontrados}")

# C) Limpieza de archivos vacíos
eliminados = limpiar_archivos_vacios(root)
print(f"Total de archivos vacíos eliminados: {eliminados}")