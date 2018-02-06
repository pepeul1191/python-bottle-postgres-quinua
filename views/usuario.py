#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request,response
from models.usuario import Usuario
from config.middleware import enable_cors

usuario_view = Bottle()

@usuario_view.route('/listar', method='GET')
@enable_cors
def listar():
  return json.dumps(Usuario().listar())


@usuario_view.route('/validar', method=['OPTIONS', 'POST'])
@enable_cors
def validar():
  usuario = request.query.usuario
  contrasenia = request.query.contrasenia
  return str(Usuario().validar(usuario, contrasenia))