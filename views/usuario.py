#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from models.usuario import usuario_listar
from config.database import connection

usuario_view = Bottle()

@usuario_view.route('/listar', method='GET')
def listar():
  print(usuario_listar())
  return 'XD'