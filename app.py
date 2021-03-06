#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, run, HTTPResponse, static_file, hook, response
from views.usuario import usuario_view
from views.estacion import estacion_view
from views.sensor import sensor_view

app = Bottle()

@app.route('/')
def index():
	the_body = 'Error : URI vacía'
	return HTTPResponse(status=404, body=the_body)

@app.route('/test/conexion')
def test_conexion():
	return 'Ok'

@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./static/')

if __name__ == '__main__':
	app.mount('/usuario', usuario_view)
	app.mount('/estacion', estacion_view)
	app.mount('/sensor', sensor_view)
	#app.run(host='localhost', port=3025, debug=True, reloader=True)
	#app.run(host='192.168.1.54', port=3025, debug=True, reloader=True)#casa idic
	app.run(host='192.168.1.54', port=3025, debug=False)#casa idic
	#app.run(host='localhost', port=3041, debug=True)