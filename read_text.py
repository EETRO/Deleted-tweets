import json

arq_json = open('dados.json', 'r')
dados = json.load(arq_json)
hist = dados['historico']

for i in hist:
    print(i['text'])
_