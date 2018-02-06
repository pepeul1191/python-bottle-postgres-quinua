require 'sinatra'
require 'httparty'
require 'sequel'
require 'pg'

Sequel::Model.plugin :json_serializer
DB = Sequel.connect('postgres://postgres:ulima@200.11.49.103:5432/quinua')

class Usuario < Sequel::Model(DB[:usuario])

end

set :bind, '192.168.1.54'
set :port, 3025

before do
  headers['Access-Control-Allow-Origin'] = '*'
  headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
  headers['Content-type'] = 'text/html; charset=UTF-8'
  headers['server'] = 'Ruby, Ubuntu'
end

post '/validar' do
	response = HTTParty.post('http://192.168.1.54:3025/usuario/validar?usuario=r&contrasenia=1')
	puts response.body, response.code, response.message, response.headers.inspect
	response.body
end

post '/usuario/validar' do 
	Usuario.where(:username => params['usuario'], :password => params['contrasenia']).count().to_s
end

get '/usuario/listar' do 
	Usuario.all().to_a.to_json
end