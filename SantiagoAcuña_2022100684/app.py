from flask import Flask
from SantiagoAcuña_2022100684.login import login
from SantiagoAcuña_2022100684.logout import logout



app = Flask(__name__)

# Expose the login blueprint
app.register_blueprint(login)
app.register_blueprint(logout)

@app.route('/', methods=['GET'])
def unida():
    return 'Server is running on port 5003!'

if __name__ == '__main__':
    app.run(debug=True, port=5003, host=localhost) 