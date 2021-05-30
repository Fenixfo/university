from flask  import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
data={}

@app.route('/', methods=['POST'])
def receive_data():
  # Se obtiene el Hashtag
  hashtag = request.form['hashtag']
  # Se obtiene el número de veces
  count = request.form['count']
  # Se agrega al array del hashtag el valor del número de veces
  data[hashtag] = count
  # Se visualiza por consola
  print('Hashtag detectado',hashtag,count)
  # Se retorna que se recibió el HashTag
  return 'Hashtag received'

@app.route('/dashboard')
def dashboard():
  return data


app.run('0.0.0.0')

