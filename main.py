from fastapi import FastAPI

app = FastAPI()

concursos = {
    1: {"concurso": "1", "dezenas": "01,02,03,04,05"},
    2: {"concurso": "2", "dezenas": "01,02,03,04,06"},
    3: {"concurso": "3", "dezenas": "01,02,03,04,07"},
    4: {"concurso": "4", "dezenas": "01,02,03,04,08"}
}


@app.get("/")
def home():
    return {"Total concurso cadastrado": len(concursos)}


@app.get("/concurso/{id_concurso}")
def get_concurso(id_concurso: int):
    if id_concurso in concursos:
        return concursos[id_concurso]
    else:
        return {"Erro": "Concurso Inexistente"}
