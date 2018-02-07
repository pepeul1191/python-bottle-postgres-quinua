from config.database import DB

class Sensor(DB):
  def maximo_minimo_promedio_rango_fechas(self, sensor_id, fecha_inicio, fecha_fin):
    self.cursor.execute("""
      SELECT to_char(fec_med, 'YYYY') || '/' || to_char(fec_med, 'MM') || '/' || to_char(fec_med, 'DD') AS dia, 
      AVG(valor_med) AS promedio, MAX(valor_med) AS maximo, MIN(valor_med) AS minimo, COUNT(valor_med) AS mediciones 
      FROM inve_instru_dato WHERE fec_med > %s AND fec_med < %s AND ide_sensor = %s
      GROUP BY dia;
    """, (fecha_inicio, fecha_fin, sensor_id))
    rs = self.cursor.fetchall()
    self.cursor.close()
    self.connection.close()
    rpta = []
    for r in rs:
      tmp = {'dia': r['dia'], 'maximo': float(r['maximo']), 'minimo': float(r['minimo']), 'promedio': float(r['promedio']), 'mediciones': r['mediciones']}
      rpta.append(tmp)
    return rpta