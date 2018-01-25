#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from sqlalchemy.sql import select
from config.models import UnidadMedida
from config.database import engine, session_db

unidad_medida_view = Bottle()

@unidad_medida_view.route('/listar', method='GET')
def listar():
	conn = engine.connect()
	stmt = select([UnidadMedida])
	return json.dumps([dict(r) for r in conn.execute(stmt)])

@unidad_medida_view.route('/listar_select', method='GET')
def listar_select():
	conn = engine.connect()
	stmt = select([UnidadMedida])
	rpta = []
	for r in conn.execute(stmt):
		t = {'id': r[0], 'nombre': r[1] + ', ' + r[2]}
		rpta.append(t)
	return json.dumps(rpta)

@unidad_medida_view.route('/guardar', method='POST')
def guardar():
	data = json.loads(request.query.data)
	nuevos = data['nuevos']
	editados = data['editados']
	eliminados = data['eliminados']
	array_nuevos = []
	rpta = None
	session = session_db()
	try:
		if len(nuevos) != 0:
			for nuevo in nuevos:
				temp_id = nuevo['id']
				nombre = nuevo['nombre']
				simbolo = nuevo['simbolo']
				s = UnidadMedida(nombre = nombre, simbolo = simbolo)
				session.add(s)
				session.flush()
				temp = {'temporal' : temp_id, 'nuevo_id' : s.id}
				array_nuevos.append(temp)
		if len(editados) != 0:
			for editado in editados:
				session.query(UnidadMedida).filter_by(id = editado['id']).update(editado)
		if len(eliminados) != 0:
			for id in eliminados:
				session.query(UnidadMedida).filter_by(id = id).delete()
		session.commit()
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado los cambios en los unidades de medida', array_nuevos]}
	except Exception as e:
		session.rollback()
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la tabla de unidades de medida', str(e)]}
	return json.dumps(rpta)