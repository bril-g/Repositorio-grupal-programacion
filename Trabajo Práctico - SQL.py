import sqlite3

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"{self.nombre} - {self.nacionalidad}"

class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} ({self.anio_publicacion}) - Autor: {self.autor.nombre}"

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        nacionalidad TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        anio INTEGER,
        autor_id INTEGER,
        FOREIGN KEY (autor_id) REFERENCES autores(id)
    )
''')

def registrar_autor(nombre, nacionalidad):
    cursor.execute('''
        INSERT INTO autores (nombre, nacionalidad)
        VALUES (?, ?)
    ''', (nombre, nacionalidad))

    conexion.commit()

    cursor.execute('SELECT MAX(id) FROM autores')
    resultado = cursor.fetchone()

    return resultado[0]

def registrar_libro(titulo, anio, autor_id):
    cursor.execute('''
        INSERT INTO libros (titulo, anio, autor_id)
        VALUES (?, ?, ?)
    ''', (titulo, anio, autor_id))
    
    conexion.commit()
  
def listar_libros():
    cursor.execute('''
        SELECT libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''')

    datos = cursor.fetchall()

    for dato in datos:
        print(f'Titulo: {dato[0]} | Año: {dato[1]} | Nombre del autor: {dato[2]}')

def actualizar_titulo_libro(id_libro, nuevo_titulo):
    cursor.execute(
        'UPDATE libros SET titulo = ? WHERE id = ?',
        (nuevo_titulo, id_libro)
    )

    conexion.commit()

def eliminar_libro(id_libro):
    cursor.execute(
        'DELETE FROM libros WHERE id = ?',
        (id_libro,)
    )

    conexion.commit()

if __name__ == "__main__":
    # Registrar un autor
    autor_id = registrar_autor("Julio Cortázar", "Argentina")
    print("ID del autor:", autor_id)

    # Registrar un libro
    registrar_libro("Rayuela", 1963, autor_id)

    # Obtener el ID del libro recién registrado
    cursor.execute("SELECT MAX(id) FROM libros")
    resultado = cursor.fetchone()
    libro_id = resultado[0]

    # Mostrar los libros registrados
    print("\nLibros registrados:")
    listar_libros()

    # Actualizar el titulo de un libro
    actualizar_titulo_libro(libro_id, "Rayuela - Edición nueva")
    print("\nDespués de actualizar:")
    listar_libros()

    # Eliminar un libro
    eliminar_libro(libro_id)
    print("\nDespués de eliminar:")
    listar_libros()

    # Probar las clases y el método __str__
    autor = Autor(autor_id, "Julio Cortázar", "Argentina")
    libro = Libro(libro_id, "Rayuela", 1963, autor)

    print("\nPrueba de __str__:")
    print(autor)
    print(libro)

conexion.close()
