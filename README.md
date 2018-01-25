## Quinua Python Postgres

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

Instalación de dependencias:

	$ sudo pip install -r requirements.txt

### Fuentes:

+ https://bottlepy.org/docs/dev/
+ http://www.sqlalchemy.org/
+ http://docs.sqlalchemy.org/en/latest/orm/mapping_columns.html

Sequel.connect(:adapter=>'sqlite', :database=>File.expand_path('../../../db/db_quinua.db', __FILE__))
Sequel.connect('postgres://postgres:ulima@168.121.220.36:5432/quinua')

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
