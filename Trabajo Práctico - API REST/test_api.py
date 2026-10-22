import requests

URL = 'http://127.0.0.1:5000'

# 1. GET: listar todos los libros
print('\n--- GET: Listar libros ---')
respuesta = requests.get(f'{URL}/api/libros')
print(respuesta.status_code)
print(respuesta.json())


# 2. POST: registrar un libro
print('\n--- POST: Registrar libro ---')
datos = {
    'titulo': 'Libro de prueba',
    'anio': 2025,
    'autor_id': 1
}

respuesta = requests.post(
    f'{URL}/api/libros',
    json=datos
)

print(respuesta.status_code)
print(respuesta.json())

# Guardamos el ID del libro creado para las siguientes pruebas
if respuesta.status_code == 201:
    libro_id = respuesta.json()['id']

    # 3. GET: consultar el libro registrado
    print('\n--- GET: Consultar un libro ---')
    respuesta = requests.get(f'{URL}/api/libros/{libro_id}')
    print(respuesta.status_code)
    print(respuesta.json())

    # 4. PUT: actualizar el libro
    print('\n--- PUT: Actualizar libro ---')
    datos_actualizados = {
        'titulo': 'Libro de prueba actualizado',
        'anio': 2026,
        'autor_id': 1
    }

    respuesta = requests.put(
        f'{URL}/api/libros/{libro_id}',
        json=datos_actualizados
    )

    print(respuesta.status_code)
    print(respuesta.json())

    # 5. DELETE: eliminar el libro de prueba
    print('\n--- DELETE: Eliminar libro ---')
    respuesta = requests.delete(f'{URL}/api/libros/{libro_id}')
    print(respuesta.status_code)
    print(respuesta.json())

    # 6. GET: comprobar que el libro fue eliminado
    print('\n--- GET: Comprobar eliminación ---')
    respuesta = requests.get(f'{URL}/api/libros/{libro_id}')
    print(respuesta.status_code)
    print(respuesta.json())


# 7. POST: probar datos incompletos
print('\n--- POST: Datos incompletos ---')
datos_incompletos = {
    'titulo': 'Libro sin datos completos'
}

respuesta = requests.post(
    f'{URL}/api/libros',
    json=datos_incompletos
)

print(respuesta.status_code)
print(respuesta.json())


# 8. GET: buscar un libro inexistente
print('\n--- GET: Libro inexistente ---')
respuesta = requests.get(f'{URL}/api/libros/999999')
print(respuesta.status_code)
print(respuesta.json())


# 9. PUT: intentar actualizar un libro inexistente
print('\n--- PUT: Libro inexistente ---')
datos_actualizados = {
    'titulo': 'Libro inexistente',
    'anio': 2026,
    'autor_id': 1
}

respuesta = requests.put(
    f'{URL}/api/libros/999999',
    json=datos_actualizados
)

print(respuesta.status_code)
print(respuesta.json())


# 10. DELETE: intentar eliminar un libro inexistente
print('\n--- DELETE: Libro inexistente ---')
respuesta = requests.delete(f'{URL}/api/libros/999999')
print(respuesta.status_code)
print(respuesta.json())