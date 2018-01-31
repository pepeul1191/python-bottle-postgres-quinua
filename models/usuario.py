from config.database import DB

class Usuario(DB):
  def listar(self):
    self.cursor.execute("""
      SELECT * FROM usuario;
    """)
    rs = self.cursor.fetchall()
    self.cursor.close()
    self.connection.close()
    return [dict(r) for r in rs]

  def validar(self, usuario, contrasenia):
    rs = 0
    self.cursor.execute("""
      SELECT COUNT(*) AS cantidad FROM usuario WHERE 
      username = %s AND password = %s;
    """, (usuario, contrasenia))
    rs = self.cursor.fetchone()
    self.cursor.close()
    self.connection.close()
    return rs['cantidad']