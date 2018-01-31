#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from models.usuario import Usuario

usuario_view = Bottle()

@usuario_view.route('/listar', method='GET')
def listar():
  return json.dumps(Usuario().listar())

@usuario_view.route('/validar', method=['OPTIONS', 'POST'])
def validar():
  usuario = request.query.usuario
  contrasenia = request.query.contrasenia
  return str(Usuario().validar(usuario, contrasenia))