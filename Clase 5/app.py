from flask import Flask
from app import login
from logout import logout



app = Flask(__name__)

# Expose the login blueprint
app.register_blueprint(login)
app.register_blueprint(logout)

@app.route('/', methods=['GET'])
def unida():
    return 'Server is running on port 5000!'

if __name__ == '__main__':
    # The 0.0.0.0 host allows the application to be accessible from any IP address
    # El 0.0.0.0 permite que la aplicación sea accesible desde cualquier dirección IP
    app.run(debug=True, port=5000, host='0.0.0.0') # Cambia el puerto y host según sea necesario