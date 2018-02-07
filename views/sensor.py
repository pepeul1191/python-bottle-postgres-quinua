#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request,response
from models.sensor import Sensor
from config.middleware import enable_cors

sensor_view = Bottle()

@sensor_view.route('/maximo_minimo_promedio_rango_fechas', method='GET')
@enable_cors
def maximo_minimo_promedio_rango_fechas():
  sensor_id = request.query.sensor_id
  fecha_inicio = request.query.fecha_inicio
  fecha_fin = request.query.fecha_fin
  return json.dumps(Sensor().maximo_minimo_promedio_rango_fechas(sensor_id, fecha_inicio, fecha_fin))