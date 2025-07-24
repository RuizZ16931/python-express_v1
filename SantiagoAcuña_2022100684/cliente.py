from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def obtener_datos_cliente():

    print("-> Petición POST recibida en /cliente")

    datos_entrada = request.get_json()

    if not datos_entrada or 'ci' not in datos_entrada:
        print("Error: La solicitud no contenía el JSON esperado.")
        # Si no hay datos o falta la 'ci', devolvemos un error.
        return jsonify({
            "accion": "Solicitud inválida",
            "codRes": "ERROR",
            "menRes": "Cuerpo de la solicitud vacío o sin la clave 'ci'.",
        }), 400 
    
    cedula_recibida = datos_entrada['ci']
    print(f"Cédula recibida para buscar: {cedula_recibida}")

    if cedula_recibida in clientes_db:
        print(f"Cliente encontrado: {cedula_recibida}")
        datos_del_cliente = clientes_db[cedula_recibida]
        
        respuesta_exitosa = {
            "accion": "exito",
            "codRes": "sin errores",
            "menRes": "OK",
            "ci": cedula_recibida,
            "nombre": datos_del_cliente["nombre"],
            "apellidos": datos_del_cliente["apellidos"]
        }
        return jsonify(respuesta_exitosa), 200
    else:
        print(f"Cliente NO encontrado: {cedula_recibida}")
        respuesta_error = {
            "accion": "Cliente no existe",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": cedula_recibida
        }
        return jsonify(respuesta_error), 404