from config.database import connection

def usuario_listar():
  cur = connection.cursor()
  cur.execute("SELECT * FROM usuario;")
  rs = cur.fetchall()
  cur.close()
  connection.close()
  return rs