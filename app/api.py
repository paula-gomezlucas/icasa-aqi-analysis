from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from localizacion import localizacion
from usuario import usuario


class Login(BaseModel):
    email: str
    password: str


class Signup(BaseModel):
    email: str
    password: str
    nombre: str


class Actualizacion(BaseModel):
    email: str
    upd: bool


class Consulta(BaseModel):
    email: str


class Vivienda(BaseModel):
    titulo: str
    ica: int  # o lo que sea


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/login")
async def login(data: Login):
    user = usuario(None, data.password, data.email, None)
    if user.acceder():
        return {"rol": user.esGestor, "status": True}
    else:
        return {"rol": False, "status": False}


@app.post("/signup")
async def signup(data: Signup):
    user = usuario(data.nombre, data.password, data.email, None)
    return {"registrado": usuario.registroBBDD(user)}


@app.post("/actualizacion")
async def actualizacion(data: Actualizacion):
    user = usuario(None, None, None, None)
    usuario.altaBaja(user, data.email, data.upd)


@app.post("/consulta")
async def consulta(data: Consulta):
    name = usuario.accesoBBDD(data.email)
    if name is None:
        return{"nombre": ""}
    else:
        return{"nombre": name}


@app.post("/icas")
async def icas(viviendas: List[Vivienda]):

    url = viviendas[0].titulo
    viviendas.pop(0)
    for v in viviendas:
        # sacar la parte de la string
        cadena = v.titulo.split(" en ")[1]
        loc = localizacion(cadena, url)
        v.ica = loc.zona_ica().ica

    # devolvemos la lista de vivienda tal cual, solo que ahora tienen actualizados los valores ICA
    return viviendas
