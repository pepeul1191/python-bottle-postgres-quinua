#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request,response
from models.sensor import Sensor
from config.middleware import enable_cors

sensor_view = Bottle()

#http://192.168.1.54:3025/sensor/maximo_minimo_promedio_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
@sensor_view.route('/maximo_minimo_promedio_rango_fechas', method='GET')
@enable_cors
def maximo_minimo_promedio_rango_fechas():
  sensor_id = request.query.sensor_id
  fecha_inicio = request.query.fecha_inicio
  fecha_fin = request.query.fecha_fin
  return json.dumps(Sensor().maximo_minimo_promedio_rango_fechas(sensor_id, fecha_inicio, fecha_fin))

#http://192.168.1.54:3025/sensor/promedio_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
@sensor_view.route('/promedio_rango_fechas', method='GET')
@enable_cors
def promedio_rango_fechas():
  sensor_id = request.query.sensor_id
  fecha_inicio = request.query.fecha_inicio
  fecha_fin = request.query.fecha_fin
  return json.dumps(Sensor().promedio_rango_fechas(sensor_id, fecha_inicio, fecha_fin))

#http://192.168.1.54:3025/sensor/maximo_minimo_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
@sensor_view.route('/maximo_minimo_rango_fechas', method='GET')
@enable_cors
def maximo_minimo_rango_fechas():
  sensor_id = request.query.sensor_id
  fecha_inicio = request.query.fecha_inicio
  fecha_fin = request.query.fecha_fin
  return json.dumps(Sensor().maximo_minimo_rango_fechas(sensor_id, fecha_inicio, fecha_fin))

#http://192.168.1.54:3025/sensor/rango_tiempo_dia?dia_medicion=2017-08-18&sensor_id=3&hora_inicio=00:00&hora_fin=00:14 
@sensor_view.route('/rango_tiempo_dia', method='GET')
@enable_cors
def rango_tiempo_dia():
  sensor_id = request.query.sensor_id
  hora_inicio = request.query.hora_inicio
  hora_fin = request.query.hora_fin
  dia_medicion = request.query.dia_medicion
  return json.dumps(Sensor().rango_tiempo_dia(sensor_id, dia_medicion, hora_inicio, hora_fin))