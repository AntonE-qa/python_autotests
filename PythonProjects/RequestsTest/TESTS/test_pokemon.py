import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '06be53cf7a29caf1e80f24497d157b8d'}

def test_get_trainers_by_level():

    """
    Тест на код 200
    """

    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():

    """
    Тест на id
    """

    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3704}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'   