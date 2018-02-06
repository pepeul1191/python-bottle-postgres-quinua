import bottle
from bottle import response

def enable_cors(fn):
  def _enable_cors(*args, **kwargs):
    # set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    response.headers['server'] = 'Ubuntu,Python'
    if bottle.request.method != 'OPTIONS':
      # actual request; reply with the actual response
      return fn(*args, **kwargs)
  return _enable_cors