import pandas as pd
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def teste():
  return 'Funcionando...'

@app.route('/premier')
def premier():
  with open("./premierleague/premierleague.json", encoding='utf-8') as       premierleague_json:
    dados = json.load(premierleague_json)
  return jsonify(dados)


@app.route('/premierleague')
def premierleague():

  premierleague = pd.read_csv('./premierleague/premierleague.csv')
  linha = premierleague.loc[0] #usando apenas uma linha das repetições
  #usar dicionário. não está funcionando
  return jsonify(linha)

app.run(host='0.0.0.0') #padrão de host sugerido pelo Replit para usar em seus servidores