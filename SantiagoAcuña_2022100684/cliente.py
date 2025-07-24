# Importamos las herramientas de Flask que necesitamos, como se ve en la Clase 4.
from flask import Blueprint, request, jsonify

# Creamos un Blueprint, que es como un mini-aplicativo para organizar nuestras rutas.
# Este archivo debe llamarse 'cliente.py'.
cliente = Blueprint('cliente', __name__)

# --- Simulación de Base de Datos (sin usar una base de datos real) ---
# Usamos un diccionario de Python para guardar los datos, como viste en tus clases.
# La "key" (clave) es la cédula y el "value" (valor) es otro diccionario con los datos.
clientes_db = {
    "5478271": {
        "nombre": "Santiago",
        "apellidos": "Ruiz Diaz"
    },
    # Puedes agregar más clientes aquí si quieres
    "1234567": {
        "nombre": "Maria",
        "apellidos": "Gomez"
    }
}
# ------------------------------------


# Definimos la ruta '/cliente' que aceptará peticiones POST.
@cliente.route('/cliente', methods=['POST'])
def obtener_datos_cliente():
    """
    Este es el servicio que busca un cliente por su cédula.
    Recibe un JSON como: {"ci": "5478271"}
    """
    print("-> Petición POST recibida en /cliente")

    # 1. Obtenemos los datos JSON que nos envía el cliente (por ejemplo, desde SoapUI).
    datos_entrada = request.get_json()

    # Verificamos si los datos llegaron correctamente.
    if not datos_entrada or 'ci' not in datos_entrada:
        print("Error: La solicitud no contenía el JSON esperado.")
        # Si no hay datos o falta la 'ci', devolvemos un error.
        return jsonify({
            "accion": "Solicitud inválida",
            "codRes": "ERROR",
            "menRes": "Cuerpo de la solicitud vacío o sin la clave 'ci'.",
        }), 400 # El código 400 significa "Bad Request" (Solicitud incorrecta).

    # 2. Sacamos la cédula del JSON.
    cedula_recibida = datos_entrada['ci']
    print(f"Cédula recibida para buscar: {cedula_recibida}")

    # 3. Usamos un condicional 'if' para buscar la cédula en nuestro diccionario 'clientes_db'.
    #    El operador 'in' comprueba si la clave existe en el diccionario.
    if cedula_recibida in clientes_db:
        # Si la cédula SÍ existe en nuestro diccionario...
        print(f"Cliente encontrado: {cedula_recibida}")
        datos_del_cliente = clientes_db[cedula_recibida]
        
        # Preparamos la respuesta de éxito tal como se pidió.
        respuesta_exitosa = {
            "accion": "exito",
            "codRes": "sin errores",
            "menRes": "OK",
            "ci": cedula_recibida,
            "nombre": datos_del_cliente["nombre"],
            "apellidos": datos_del_cliente["apellidos"]
        }
        # Devolvemos el JSON de éxito con el código 200 (OK).
        return jsonify(respuesta_exitosa), 200
    else:
        # Si la cédula NO existe...
        print(f"Cliente NO encontrado: {cedula_recibida}")
        
        # Preparamos la respuesta de error tal como se pidió.
        respuesta_error = {
            "accion": "Cliente no existe",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": cedula_recibida
        }
        # Devolvemos el JSON de error con el código 404 (Not Found).
        return jsonify(respuesta_error), 404