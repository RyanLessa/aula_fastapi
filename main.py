from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from aula_fastapi.routes import router

app = FastAPI()

app.include_router(router, prefix='/users')

@app.get('/check')
def main():
    return HTMLResponse('<h1>Olá mundo</h1>')
