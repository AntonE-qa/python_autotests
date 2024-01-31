"""
Pokemons test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '06be53cf7a29caf1e80f24497d157b8d'}

"""
Создание покемона
"""

#body = {
#    "name": "Spider",
#    "photo": "https://dolnikov.ru/pokemons/albums/068.png"
#}

#response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
#print(response)

"""
Смена имени покемона
"""

#body = {
#   "pokemon_id": "29077",
#   "name": "Turbo",
#   "photo": "https://dolnikov.ru/pokemons/albums/009.png"
#}

#response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
#print(response)

"""
Поймать покемона в покебол
"""
#body = {
#    "pokemon_id": "29077"
#}

#response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
#print(response)