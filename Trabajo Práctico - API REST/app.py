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

conexion = sqlite3.connect('biblioteca.db', check_same_thread=False)
cursor = conexion.cursor()

print("Base de datos utilizada:", conexion.execute("PRAGMA database_list").fetchall())
print("Autores encontrados:", cursor.execute("SELECT * FROM autores").fetchall())

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


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/autores', methods=['GET'])
def obtener_autor_db():
    cursor.execute('SELECT * FROM autores')
    autores = cursor.fetchall()

    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def insertar_autor_db():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'nacionalidad' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400

    cursor.execute('''
        INSERT INTO autores (nombre, nacionalidad)
        VALUES (?, ?)
    ''', (datos['nombre'], datos['nacionalidad']))

    conexion.commit()

    cursor.execute('SELECT MAX(id) FROM autores')
    resultado = cursor.fetchone()
    id_autor = resultado[0]

    nuevo_autor = {
        'id': id_autor,
        'nombre': datos['nombre'],
        'nacionalidad': datos['nacionalidad']
    }

    return jsonify(nuevo_autor), 201

@app.route('/api/libros', methods=['GET'])
def obtener_libros_db():
    cursor.execute('''
        SELECT libros.titulo, libros.anio, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    ''')

    datos = cursor.fetchall()

    return jsonify(datos), 200

@app.route('/api/libros/<int:libro_id>', methods=['GET'])
def obtener_libro(libro_id):
    cursor.execute('SELECT * FROM libros WHERE id = ?', (libro_id,))
    libro = cursor.fetchone()

    if libro:
        return jsonify(libro), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

@app.route('/api/libros', methods=['POST'])
def insertar_libro_db():
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400

    cursor.execute('''
        INSERT INTO libros (titulo, anio, autor_id)
        VALUES (?, ?, ?)
    ''', (datos['titulo'], datos['anio'], datos['autor_id']))

    conexion.commit()

    cursor.execute('SELECT MAX(id) FROM libros')
    resultado = cursor.fetchone()
    libro_id = resultado[0]

    nuevo_libro = {
        'id': libro_id,
        'titulo': datos['titulo'],
        'anio': datos['anio'],
        'autor_id': datos['autor_id']
    }

    return jsonify(nuevo_libro), 201

@app.route('/api/libros/<int:libro_id>', methods=['PUT'])
def actualizar_libro_db(libro_id):
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({'error': 'Datos incompletos'}), 400

    cursor.execute('SELECT * FROM libros WHERE id = ?', (libro_id,))
    libro = cursor.fetchone()

    if libro:
        cursor.execute('''
        UPDATE libros 
        SET titulo = ?, anio = ?, autor_id = ? 
        WHERE id = ?
        ''', (datos['titulo'], datos['anio'], datos['autor_id'], libro_id))

        conexion.commit()

        cursor.execute('SELECT * FROM libros WHERE id = ?', (libro_id,))
        libro = cursor.fetchone()

        return jsonify(libro), 200

    return jsonify({'error': 'Libro no encontrado'}), 404

@app.route('/api/libros/<int:libro_id>', methods=['DELETE'])
def eliminar_libro_db(libro_id):
    cursor.execute('SELECT * FROM libros WHERE id = ?', (libro_id,))
    libro = cursor.fetchone()

    if libro:
        cursor.execute('DELETE FROM libros WHERE id = ?', (libro_id,))

        conexion.commit()

        return jsonify(libro), 200

    return jsonify({'error': 'Libro no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)