import json

ARQUIVO = "noticias.json"

def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(vingadores):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(noticias, arquivo, indent=4, ensure_ascii=False)