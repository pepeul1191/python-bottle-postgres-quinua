#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request,response
from models.estacion import Estacion
from config.middleware import enable_cors

estacion_view = Bottle()

@estacion_view.route('/listar', method='GET')
@enable_cors
def listar():
  return json.dumps(Estacion().listar())

@estacion_view.route('/detalle/<estacion_id>', method='GET')
@enable_cors
def detalle(estacion_id):
  return json.dumps(Estacion().detalle(estacion_id))