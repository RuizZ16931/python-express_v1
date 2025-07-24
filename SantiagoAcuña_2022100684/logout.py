from flask import Blueprint, Flask, jsonify, request
import logging

logout = Blueprint('logout', __name__)

@logout.route('/logout', methods=['POST'])
def llamarServiciosSet():
    user = request.json.get('user')
    password = request.json.get('password')
    print("User enviado: ", user, "Password enviado: ", password)
    
