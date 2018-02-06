from config.database import DB
from decimal import Decimal

class Estacion(DB):
  def listar(self):
    self.cursor.execute("""
      SELECT ide_estacion, latitud, longitud FROM inve_estacion;
    """)
    rs = self.cursor.fetchall()
    self.cursor.close()
    self.connection.close()
    rpta = []
    for r in rs:
      tmp = {'ide_estacion': int(r['ide_estacion']), 'longitud': float(r['longitud']), 'latitud': float(r['latitud'])}
      rpta.append(tmp)
    return rpta

  def detalle(self, estacion_id):
    rs = 0
    self.cursor.execute("""
      SELECT IE.nombre_estacion, II.ide_sensor, IE.descripcion, II.nombre_sensor, II.desc_instrumento, MTT.des_tipo FROM inve_estacion IE 
      INNER JOIN inve_estacion_instru IEI ON IE.ide_estacion = IEI.ide_estacion 
      INNER JOIN inve_instru II ON II.ide_sensor = IEI.ide_sensor 
      INNER JOIN mae_tablatipo_tipo MTT ON MTT.ide_tipo = II.fk_tipo_unidad_medida 
      WHERE IEI.ide_estacion = %s
    """, [estacion_id])
    rs = self.cursor.fetchall()
    self.cursor.close()
    self.connection.close()
    rpta = []
    for r in rs:
      tmp = {'nombre_estacion': r['nombre_estacion'], 'ide_sensor': float(r['ide_sensor']), 'descripcion': r['descripcion'], 'desc_instrumento': r['desc_instrumento'], 'des_tipo': r['des_tipo']}
      rpta.append(tmp)
    return rpta