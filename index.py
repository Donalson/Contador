#Importacion de flask para crear y ejecutar sitio web
from flask import Flask

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)

#Creacion de la ruta principal del sitio web y texto de prueba
@app.route('/')
def home():
    return 'Hola Mundo'

#Inializacion del sitio web para correr
if __name__ == '__main__':
    app.run()