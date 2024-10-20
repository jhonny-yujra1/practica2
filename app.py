from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
       
        return render_template('resultado.html', tipo='Inscripción de Curso', datos={'Nombre': nombre, 'Apellido': apellido, 'Curso': curso})
    return render_template('formulario1.html')

@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        return render_template('resultado.html', tipo='Registro de Usuario', datos={'Nombre': nombre, 'Apellido': apellido, 'Correo': correo})
    return render_template('formulario2.html')

@app.route('/formulario3', methods=['GET', 'POST'])
def formulario3():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return render_template('resultado.html', tipo='Registro de Productos', datos={'Producto': producto, 'Categoría': categoria, 'Existencia': existencia, 'Precio': precio})
    return render_template('formulario3.html')

@app.route('/formulario4', methods=['GET', 'POST'])
def formulario4():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return render_template('resultado.html', tipo='Registro de Libros', datos={'Título': titulo, 'Autor': autor, 'Resumen': resumen, 'Medio': medio})
    return render_template('formulario4.html')

if __name__ == '__main__':
    app.run(debug=True)