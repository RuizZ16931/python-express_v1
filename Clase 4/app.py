#-*- Coding: utf-8 -*-
"""
el utf-8 es un formato de codificación 
de caracteres que permite representar todos los caracteres del alfabeto latino 
y muchos otros caracteres de diferentes idiomas.
""" 
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def unida():
    return 'Hola Mundo desde la unida'

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') # Cambia el puerto y host según sea necesario

""""
eL O.0.0.0 permite que la aplicación sea accesible desde cualquier dirección IP
"""