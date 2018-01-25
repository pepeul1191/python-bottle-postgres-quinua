#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from sqlalchemy.sql import select
from config.models import Sensor
from config.database import engine, session_db

sensor_view = Bottle()

@sensor_view.route('/listar', method='GET')
def listar():
	conn = engine.connect()
	stmt = select([Sensor])
	return json.dumps([dict(r) for r in conn.execute(stmt)])

@sensor_view.route('/listar/<estacion_id>', method='GET')
def listar_estacion(estacion_id):
	conn = engine.connect()
	stmt = """
		SELECT S.id, S.nombre, S.descripcion, (U.nombre || ',' || U.simbolo) AS unidad_medida, S.unidad_medida_id 
		FROM sensores S INNER JOIN unidad_medidas U ON U.id = S.unidad_medida_id
		WHERE S.estacion_id = :estacion_id
		"""
	return json.dumps([dict(r) for r in conn.execute(stmt, {'estacion_id' : estacion_id})])

@sensor_view.route('/guardar', method='POST')
def guardar():
	data = json.loads(request.query.data)
	nuevos = data['nuevos']
	editados = data['editados']
	eliminados = data['eliminados']
	estacion_id = data['extra']['estacion_id']
	array_nuevos = []
	rpta = None
	session = session_db()
	try:
		if len(nuevos) != 0:
			for nuevo in nuevos:
				temp_id = nuevo['id']
				nombre = nuevo['nombre']
				descripcion = nuevo['descripcion']
				unidad_medida_id = nuevo['unidad_medida_id']
				s = Sensor(nombre = nombre, descripcion = descripcion, unidad_medida_id = unidad_medida_id, estacion_id = estacion_id)
				session.add(s)
				session.flush()
				temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
				array_nuevos.append(temp)
		if len(editados) != 0:
			for editado in editados:
				session.query(Sensor).filter_by(id = editado['id']).update(editado)
		if len(eliminados) != 0:
			for id in eliminados:
				session.query(Sensor).filter_by(id = id).delete()
		session.commit()
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los sensores', array_nuevos]}
	except Exception as e:
		session.rollback()
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar los sensores', str(e)]}
	return json.dumps(rpta)