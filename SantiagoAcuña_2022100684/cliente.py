from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def obtener_datos_cliente():

    print("-> Petición POST recibida en /cliente")

    # 1. Obtenemos los datos JSON que nos envía el cliente (SoapUI).
    datos_entrada = request.get_json()

    # Verificamos si los datos llegaron correctamente.
    if not datos_entrada or 'ci' not in datos_entrada:
        print("Error: La solicitud no contenía el JSON esperado.")
        return jsonify({
            "accion": "Solicitud inválida",
            "codRes": "ERROR",
            "menRes": "Cuerpo de la solicitud vacío o sin la clave 'ci'.",
        }), 400

    # 2. Sacamos la cédula del JSON.
    cedula_recibida = datos_entrada['ci']
    print(f"Cédula recibida para buscar: {cedula_recibida}")

    # 3. Llamamos a nuestra función de lógica, igual que en tu ejemplo de login.
    #    Esta función nos devolverá todos los datos para la respuesta.
    respuesta_dict = verificar_cliente(cedula_recibida)
    
    # El código de estado (200 o 404) dependerá si el cliente fue encontrado.
    status_code = 200 if respuesta_dict["codRes"] == "sin errores" else 404

    # 4. Devolvemos la respuesta en formato JSON.
    return jsonify(respuesta_dict), status_code


# Esta función contiene la lógica de verificación.
# Es similar a tu 'inicializarVariables' del ejemplo de login.
def verificar_cliente(ci_a_verificar):
    """
    Verifica si la cédula corresponde a un cliente válido.
    """
    # Aquí definimos los datos del cliente válido, sin usar un diccionario global.
    ci_valida = "5478271"
    nombre_valido = "Santiago"
    apellidos_validos = "Ruiz Diaz"

    # Comparamos la cédula recibida con la cédula válida.
    if ci_a_verificar == ci_valida:
        # Si coinciden, preparamos la respuesta de ÉXITO.
        print(f"Cliente encontrado: {ci_a_verificar}")
        respuesta = {
            "accion": "exito",
            "codRes": "sin errores",
            "menRes": "OK",
            "ci": ci_a_verificar,
            "nombre": nombre_valido,
            "apellidos": apellidos_validos
        }
    else:
        print(f"Cliente NO encontrado: {ci_a_verificar}")
        respuesta = {
            "accion": "Cliente no existe",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci_a_verificar
        }
    return respuesta