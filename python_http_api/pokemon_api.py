import requests
import json

def getManyCards():
  url = "https://pokemon-tcg-card-prices.p.rapidapi.com/card"
  querystring = {"setId":"33ee55f4-30d0-4900-850f-36a351fb9719","set":"vivid-voltage","series":"sword-and-shield","limit":"10"}
  headers = {
    "X-RapidAPI-Host": "pokemon-tcg-card-prices.p.rapidapi.com",
    "X-RapidAPI-Key": "1ead6b9fb3msh90d4404a2b71121p1b963bjsncf4dad082546"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  #print(response.text)
  jsonData = json.loads(response.text)
  return jsonData
