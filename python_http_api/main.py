import json
from pokemon_api import getManyCards

jsonData = getManyCards()
#print(json.dumps(jsonData, indent=2))

result = jsonData['results']
for card in result:
  print(card['cardId'])
  print(card['name'])
  print(card['set'])
  print(card['setId'])
  print(card['series'])
  print(card['pokemon'])
  print('='*40)

#print(len(result))
#'cardId': '4b5f7b35-98c2-4600-8987-4f2018ea2a2f', 'name': 'Leon', 'cardNumber': '195', 'setNumber': '185', 'setId': '33ee55f4-30d0-4900-850f-36a351fb9719', 'set': 'vivid-voltage', 'series': 'sword-and-shield', 'variant': 'DEFAULT', 'superType': 'trainer', 'types': [], 'subTypes': ['supporter'], 'rarity': 'rare-rainbow', 'pokemon': [], 'artist': 'Hideki Ishikawa'
