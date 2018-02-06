## Quinua Python Postgres

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP
+ Ruby 2.3.1
+ Postgres

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate
	$ pip install -r requirements.txt
    $ python app.py

En caso de usar el servicio en ruby:

    $ sudo apt-get install libpq-dev
    $ bundler install
    $ ruby app.rb

### Fuentes:

+ https://bottlepy.org/docs/dev/
+ http://initd.org/psycopg/docs/usage.html
+ http://initd.org/psycopg/docs/cursor.html#cursor.fetchall
+ https://stackoverflow.com/questions/17262170/bottle-py-enabling-cors-for-jquery-ajax-requests

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]
