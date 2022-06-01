#Importacion de flask para crear y ejecutar sitio web, renderizar plantillas
from pdb import Restart
from flask import Flask, render_template

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)

#Variables a utilizar
Contador = 0;

#Creacion de la ruta principal del sitio web y texto de prueba
@app.route('/')
def home():
    return render_template('contador.html', contador = Contador)

#Ruta con funcion de sumar
@app.route("/Sumar")
def sumar():
    global Contador
    Contador = Contador + 1
    return render_template('contador.html', contador = Contador)

#Ruta con funcion de restar
@app.route("/Restar")
def restar():
    global Contador
    Contador = Contador - 1
    return render_template('contador.html', contador = Contador)

#Ruta con funcion de resetear
@app.route("/Reset")
def reset():
    global Contador
    Contador = 0
    return render_template('contador.html', contador = Contador)

#Inializacion del sitio web para correr(modo debug encendido para detectar cambios)
if __name__ == '__main__':
    app.run(debug=True)