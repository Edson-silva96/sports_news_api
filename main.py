from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import json 
from fastapi.middleware.cors import CORSMiddleware
from models import noticia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar o JSON do arquivo
with open("noticias.json", "r", encoding="utf-8") as arquivo:
    noticias = json.load(arquivo)


@app.get("/noticias", status_code=200)
def listar_herois():
    return noticias

@app.get("/noticias/{id_noticia}", status_code=200)
def obter_noticia(id_noticia: int):
    id_str = str(id_noticia)
    if id_str not in noticias:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return noticias[id_str]


@app.post("/noticias/adicionar", status_code=201)
def adicionar_noticia(nova_noticia: noticia):
    novo_id = str(len(noticias) + 1)

    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Gera data atual

    noticias[novo_id] = {
        **nova_noticia.dict(),
        "data": data_atual
    }

    with open("noticias.json", "w", encoding="utf-8") as arquivo:
        json.dump(noticias, arquivo, indent=4, ensure_ascii=False)

    return {"mensagem": "Notícia adicionada com sucesso!", "id": novo_id}


@app.put("/noticias/atualizar/{id_noticia}", status_code=200)
def atualizar_heroi(id_noticia: int, dados_atualizados: dict = Body(...)):
    id_str = str(id_noticia)

    if id_str not in noticias:
        raise HTTPException(status_code=404, detail="Herói não encontrado")

    noticias[id_str].update(dados_atualizados)

    with open("noticias.json", "w", encoding="utf-8") as arquivo:
        json.dump(noticias, arquivo, indent=4, ensure_ascii=False)

    return {"mensagem": "noticia atualizado com sucesso!", "id": id_str}


@app.delete("/noticias/deleter/{id_noticia}", status_code=200)
def deletar_noticia(id_noticia: int):
    id_str = str(id_noticia)

    if id_str not in noticias:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")

    # Remove da memória
    del noticias[id_str]

    # Salva de volta no arquivo
    with open("noticias.json", "w", encoding="utf-8") as f:
        json.dump(noticias, f, ensure_ascii=False, indent=4)

    return {"detail": "Notícia deletada com sucesso"}