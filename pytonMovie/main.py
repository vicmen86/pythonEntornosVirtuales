from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title= "Mi app con FastAPI"
app.version="0.0.1"
@app.get('/', tags=["Home"])
def message():
  return HTMLResponse('<h1>Hello World!</h1>')