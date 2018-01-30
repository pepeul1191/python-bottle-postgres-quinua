#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from sqlalchemy.sql import select
#from config.models import Usuario
from config.database import engine, session_db, connection

usuario_view = Bottle()

@usuario_view.route('/listar', method='GET')
def listar():
  cur = connection.cursor()
  cur.execute("SELECT * FROM usuario;")
  rs = cur.fetchall()
  print(rs)
  cur.close()
  connection.close()
  return 'XD'