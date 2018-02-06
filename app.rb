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
  DB[query].all.to_json
end