from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def obtener_datos_cliente():
    print("-> Petición POST recibida en /cliente")
    datos_entrada = request.get_json()

    if not datos_entrada or 'ci' not in datos_entrada:
        return jsonify({"menRes": "JSON inválido"}), 400

    cedula_recibida = datos_entrada['ci']
    print(f"Cédula recibida para buscar: {cedula_recibida}")

    respuesta_dict = verificar_cliente(cedula_recibida)
    
    status_code = 200 if respuesta_dict["codRes"] == "sin errores" else 404

    return jsonify(respuesta_dict), status_code

def verificar_cliente(ci_a_verificar):

    ci_valida = "5478271"
    nombre_valido = "Santiago"
    apellidos_validos = "Ruiz Diaz"

    if ci_a_verificar == ci_valida:
        respuesta = {
            "accion": "exito",
            "codRes": "sin errores",
            "menRes": "OK",
            "ci": ci_a_verificar,
            "nombre": nombre_valido,
            "apellidos": apellidos_validos
        }
    else:
        respuesta = {
            "accion": "Cliente no existe",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci_a_verificar
        }
    return respuesta