require 'sinatra'
require 'httparty'
require 'sequel'
require 'pg'

# Configuración de la base de datos

Sequel::Model.plugin :json_serializer
DB = Sequel.connect('postgres://postgres:ulima@200.11.49.103:5432/quinua')

# Modelos de la base de datos

class Usuario < Sequel::Model(DB[:usuario])

end

class Estacion < Sequel::Model(DB[:inve_estacion])

end

# Configuración del servidor

set :bind, '192.168.1.54'
set :port, 3025
set :public_folder, 'static'

before do
  headers['Access-Control-Allow-Origin'] = '*'
  headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
  headers['Content-type'] = 'text/html; charset=UTF-8'
  headers['server'] = 'Ruby, Ubuntu'
end

# Rutas del servidor

post '/usuario/validar' do 
  Usuario.where(:username => params['usuario'], :password => params['contrasenia']).count().to_s
end

get '/estacion/listar' do 
  Estacion.all().to_a.to_json
end

get '/estacion/detalle/:estacion_id' do
  query = '
    SELECT IE.nombre_estacion, II.ide_sensor, IE.descripcion, II.nombre_sensor, II.desc_instrumento, MTT.des_tipo FROM inve_estacion IE 
    INNER JOIN inve_estacion_instru IEI ON IE.ide_estacion = IEI.ide_estacion 
    INNER JOIN inve_instru II ON II.ide_sensor = IEI.ide_sensor 
    INNER JOIN mae_tablatipo_tipo MTT ON MTT.ide_tipo = II.fk_tipo_unidad_medida 
    WHERE IEI.ide_estacion = ' + params[:estacion_id]
  rs = DB[query].all
  rpta = []
  rs.each do |r|
    r[:ide_sensor] = r[:ide_sensor].to_i
    rpta.push(r)
  end
  rpta.to_json
end

get '/sensor/maximo_minimo_promedio_rango_fechas' do
  #http://192.168.1.54:3025/sensor/maximo_minimo_promedio_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
  query = "
  SELECT to_char(fec_med, 'YYYY') || '/' || to_char(fec_med, 'MM') || '/' || to_char(fec_med, 'DD') AS dia, 
  AVG(valor_med) AS promedio, MAX(valor_med) AS maximo, MIN(valor_med) AS minimo, COUNT(valor_med) AS mediciones 
  FROM inve_instru_dato WHERE fec_med > '" + params[:fecha_inicio] + "' AND fec_med < '" + params[:fecha_fin] + "' AND ide_sensor = " + params[:sensor_id].to_s + "
  GROUP BY dia;"
  rs = DB[query].all
  rpta = []
  rs.each do |r|
    r[:promedio] = r[:promedio].to_f
    r[:maximo] = r[:maximo].to_f
    r[:minimo] = r[:minimo].to_f
    rpta.push(r)
  end
  rpta.to_json
end

get '/sensor/promedio_rango_fechas' do
  #http://192.168.1.54:3025/sensor/promedio_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
  query = "
  SELECT to_char(fec_med, 'YYYY') || '/' || to_char(fec_med, 'MM') || '/' || to_char(fec_med, 'DD') AS dia, 
  AVG(valor_med) AS promedio, COUNT(valor_med) AS mediciones 
  FROM inve_instru_dato WHERE fec_med > '" + params[:fecha_inicio] + "' AND fec_med < '" + params[:fecha_fin] + "' AND ide_sensor = " + params[:sensor_id].to_s + "
  GROUP BY dia;"
  rs = DB[query].all
  rpta = []
  rs.each do |r|
    r[:promedio] = r[:promedio].to_f
    rpta.push(r)
  end
  rpta.to_json
end

get '/sensor/maximo_minimo_rango_fechas' do
  #http://192.168.1.54:3025/sensor/maximo_minimo_rango_fechas?sensor_id=1&fecha_inicio=2017-08-18&fecha_fin=2017-08-21
  query = "
  SELECT to_char(fec_med, 'YYYY') || '/' || to_char(fec_med, 'MM') || '/' || to_char(fec_med, 'DD') AS dia, 
  MAX(valor_med) AS maximo, MIN(valor_med) AS minimo, COUNT(valor_med) AS mediciones 
  FROM inve_instru_dato WHERE fec_med > '" + params[:fecha_inicio] + "' AND fec_med < '" + params[:fecha_fin] + "' AND ide_sensor = " + params[:sensor_id].to_s + "
  GROUP BY dia;"
  rs = DB[query].all
  rpta = []
  rs.each do |r|
    r[:maximo] = r[:maximo].to_f
    r[:minimo] = r[:minimo].to_f
    rpta.push(r)
  end
  rpta.to_json
end

get '/sensor/rango_tiempo_dia' do
  #http://192.168.1.54:3025/sensor/rango_tiempo_dia?dia_medicion=2017-08-18&sensor_id=3&hora_inicio=00:00&hora_fin=00:14 
  query = "
  SELECT to_char(fec_med, 'HH') || ':' || to_char(fec_med, 'MI') || ':' || to_char(fec_med, 'ss') AS momento, 
  valor_med AS dato 
  FROM inve_instru_dato WHERE fec_med > '" + params[:dia_medicion] + " " + params[:hora_inicio] + "' " +
  " AND fec_med < '" + params[:dia_medicion] + " " + params[:hora_fin] + "' AND ide_sensor = " + params[:sensor_id].to_s
  rs = DB[query].all
  rpta = []
  rs.each do |r|
    r[:dato] = r[:dato].to_f
    rpta.push(r)
  end
  rpta.to_json
end
