from flask import Response
import json
#importamos el jsoni
from flask import jsonify
#importamos flask
from flask import Flask
#iniciamos una app 
app = Flask(__name__)

#Creamos una ruta de hola mundo
@app.route("/")
def hello_World():
    return  "Hello, World!"

#Creamos una ruta con el metodo GET
@app.route("/fluxer", methods=['get'])
def fluxer_index():
    return('fluxer index')

#creamos una ruta con el metodo POST
@app.route('/fluxer', methods=['post'])
def fluxer_create():
    data = [{"message":"fluxer_created"}]
    #return('fluxer created')
    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run()