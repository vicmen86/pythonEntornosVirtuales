import store
from fastapi import FastAPI
#para responder directamente en html
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def getList():
  return [1,2,3,"mas numeros jee"]

@app.get('/contact', response_class=HTMLResponse)
def getList():
  return """
    <html>
        <head>
            <title>Codigo Html retornado</title>
        </head>
        <body>
            <h1>Hola soy una pagina!</h1>
            <p> soy un parrafo!</p>
        </body>
    </html>
    """

def run():
  store.get_categories()

#Para que corra como un script la line siguiente es fundamental
if __name__== "__main__":
  run()

