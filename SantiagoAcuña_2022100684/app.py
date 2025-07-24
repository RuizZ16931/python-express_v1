from flask import Flask
from SantiagoAcuña_2022100684 import login
from SantiagoAcuña_2022100684 import logout
from SantiagoAcuña_2022100684.cliente import cliente

app = Flask(__name__)

app.register_blueprint(login)
app.register_blueprint(logout)
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def unida():
    return 'Server is running on port 5003!'

if __name__ == '__main__':
    print("Iniciando servidor Flask en http://localhost:5003")
    app.run(debug=True, port=5003, host='localhost')