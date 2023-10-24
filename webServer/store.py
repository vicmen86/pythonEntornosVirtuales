import requests

def get_categories():
  req=requests.get('https://api.escuelajs.co/api/v1/categories')
  print(req.status_code)
  print(req.text)
  print(type(req.text))#Esto devulve tipo string
  #lo convertimos a un json
  categories=req.json()
  for category in categories:
    print(category['name'])

  