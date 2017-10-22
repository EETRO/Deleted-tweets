import json


def salvar(tweet):
    dict_salvar = {"historico": tweet}
    dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)
    arq_json = open('dados.json', 'w')
    arq_json.write(dict_salvar)
    arq_json.close()
