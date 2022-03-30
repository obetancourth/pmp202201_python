from bottle import route, run, response, request
# python -m pip install bottle
# pip install bottle
import json

# bottle --> levantar un web server, un servidor en internet que devuelve los
# recursos solicitados por medio del protocolo http o https.
# HTTP ---- GET POST
# El cliente hace un HTTP Request pormedio de un metodo
# El server responde con un Response con un estatus (200, 300 , 400, 500) y cuerpo

# URL -> https://www.unicah.edu:443/programas/index.html?viewmobile=1
#        [https] protocolo (http, https, ftp, sftp, smb, file)
#        [www.unicah.edu] domain name, nombre de dominio --X DNS
#        [443] (http 80, https 443, ftp 20, sftp 22)
#        [/programas/index.html]  uri  path o la direccion del recurso en el servidor
#        [?viewmobile=1] GET variables que sirven para actuar

# http://localhost:5000/
@route('/')
def index():
  response.content_type = "application/json"
  return json.dumps({"status":"ok","mensaje":"Api Python v1.0 PMP"})

# http://localhost:5000/suma?num1=1&num2=2
@route('/suma')
def suma():
  num1 = int(request.query["num1"])
  num2 = int(request.query["num2"])
  result = num1 + num2
  response.content_type = "application/json"
  return json.dumps({"status":"ok","resultado":result, "num1": num1, "num2": num2})

@route('/newpersona', method="POST")
def newPersona():
  nombre = request.POST.get("nombre").strip()
  telefono = request.POST.get("telefono").strip()
  email = request.POST.get("email").strip()
  # se debe guardar en una DB :P
  response.content_type = "application/json"
  return json.dumps({"status":"ok","nombre":nombre, "telefono": telefono, "email": email})


run(host="localhost", port=5000, debug=True)
