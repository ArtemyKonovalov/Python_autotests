import requests

url = 'https://api.pokemonbattle.me/v2/trainers/reg'
body = {
"trainer_token": "a09e90a8051defb85956dd8b8753d6ca",
"email": "ArtemyKonovalov.AK@yandex.ru",
"password": "5310Kent"
}
headers = {
'Content-Type': 'application/json'
}
response = requests.post(url, json=body, headers=headers)
print (response.json())



url1 = 'https://api.pokemonbattle.me/v2/pokemons'
body = {
"name": "Бульбазавр",
"photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
headers = {
'Content-Type': 'application/json',
'trainer_token': 'a09e90a8051defb85956dd8b8753d6ca'
}
response = requests.post(url1, json=body, headers=headers)
print (response.json())



url1 = 'https://api.pokemonbattle.me/v2/pokemons'
body = {
"pokemon_id": "19451",
"name": "kent"
}
headers = {
'Content-Type': 'application/json',
'trainer_token': 'a09e90a8051defb85956dd8b8753d6ca'
}
response = requests.patch(url1, json=body, headers=headers)
print (response.json())



url1 = 'https://api.pokemonbattle.me/v2/trainers/add_pokeball'
body = {
"pokemon_id": "19451"
}
headers = {
'Content-Type': 'application/json',
'trainer_token': 'a09e90a8051defb85956dd8b8753d6ca'
}
response = requests.post(url1, json=body, headers=headers)
print (response.json())





