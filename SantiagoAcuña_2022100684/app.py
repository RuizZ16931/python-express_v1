from flask import Flask
from cliente import cliente


app = Flask(__name__)

app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def unida():    
    return 'Server is running on port 5003!'

if __name__ == '__main__':
    print("Starting Flask server at http://localhost:5003")
    app.run(debug=True, port=5003, host='localhost')