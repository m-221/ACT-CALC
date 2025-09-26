from flask import Flask
app = Flask(__name__)

@app.route('/')
def hol():
    mensaje = '<h1>¡Hola bienvenidos!</h1>'
    mensaje += '<ol>'
    mensaje += '<li><h2>1.- sumar: http://127.0.0.1:5000/sumar/10/20</h2></li>'
    mensaje += '<li><h2>2.- restar: http://127.0.0.1:5000/restar/10/20</h2></li>'
    mensaje += '<li><h2>3.- dividir: http://127.0.0.1:5000/dividir/10/20</h2></li>'
    mensaje += '<li><h2>4.- multiplicar: http://127.0.0.1:5000/multiplicar/10/20</h2></li>'
    mensaje += '<li><h2>5.- maximo: http://127.0.0.1:5000/maximo/10/20</h2></li>'
    mensaje += '<li><h2>6.- minimo: http://127.0.0.1:5000/minimo/10/20</h2></li>'
    mensaje += '</ol>'
    return mensaje

@app.route('/sumar/<v1>/<v2>')
def sumar1(v1, v2):
    s = str(float(v1) + float(v2))
    mensaje = f'<h1>La suma de {v1} + {v2} es {s}</h1>'
    return mensaje

@app.route('/restar/<v1>/<v2>')
def restar1(v1, v2):
    s = str(float(v1) - float(v2))
    mensaje = f'<h1>La resta de {v1} - {v2} es {s}</h1>'
    return mensaje

@app.route('/dividir/<v1>/<v2>')
def dividir1(v1, v2):
        m = float(v1) / float(v2)
        mensaje = f'<h1>La división de {v1} / {v2} es {m}</h1>'
        return mensaje

@app.route('/multiplicar/<v1>/<v2>')
def multiplicar1(v1, v2):
    r = float(v1) * float(v2)
    mensaje = f'<h1>La multiplicación de {v1} * {v2} es {r}</h1>'
    return mensaje

@app.route('/maximo/<v1>/<v2>')
def maximo1(v1, v2):
    v1 = float(v1)
    v2 = float(v2)
    if v1 > v2:
        resultado = v1
    else:
        resultado = v2
    mensaje = f'<h1>El máximo entre {v1} y {v2} es {resultado}</h1>'
    return mensaje

@app.route('/minimo/<v1>/<v2>')
def minimo1(v1, v2):
    v1 = float(v1)
    v2 = float(v2)
    if v1 < v2:
        resultado = v1
    else:
        resultado = v2
    mensaje = f'<h1>El mínimo entre {v1} y {v2} es {resultado}</h1>'
    return mensaje
if __name__ == '__main__':
    app.run(debug=True)