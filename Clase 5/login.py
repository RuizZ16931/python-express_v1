from flask import Blueprint
from flask import Blueprint, jsonify, request


login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServiciosSet():
    user= request.json.get('user')
    password = request.json.get('password')
    print("User enviado: ",user, "Password enviado: ",password) 

    codRes, menRes, accion, rol, user = inicializarVariables(user, password)

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "usuario": user,
        "accion": accion,
        "rol": rol  # Usar el rol retornado por la función
    }

    status_code = 200 if codRes == 0 else 401
    return jsonify(salida), status_code

def inicializarVariables(user, password):
    codRes = 0
    menRes = "OK"
    accion = "login exitoso"
    rol = "Admin"  # Asignar un rol por defecto
    userLocal = "sgacuna"
    passwordLocal = "unida"

    try:
        if user == userLocal and password == passwordLocal:
            print("Login exitoso")
            accion = "login exitoso"
            rol = "Admin"  # Asignar un rol por defecto
        else:
            codRes = 1
            menRes = "Usuario o contraseña incorrectos"
            accion = "login fallido"
            rol = "N/A"
            user = "N/A"
        print("Respuesta del login:", codRes, menRes, accion, rol, user)
        return codRes, menRes, accion, rol, user
    except Exception as e:
        print("Error en el login:", e)
        codRes = 1
        menRes = "Error en el login"
        accion = "error en el login"
        rol = "N/A"
        user = "N/A"
        return codRes, menRes, accion, rol, user