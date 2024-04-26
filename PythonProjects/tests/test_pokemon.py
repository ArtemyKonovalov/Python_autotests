import requests

def test_get_trainers_status_code():
    url = 'https://api.pokemonbattle.me/v2/trainers'
    body = {
        "trainer_token": "a09e90a8051defb85956dd8b8753d6ca",
        "email": "ArtemyKonovalov.AK@yandex.ru",
        "password": "5310Kent"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, json=body, headers=headers)
    assert response.status_code == 200



    

def test_get_trainers_name():
    url = 'https://api.pokemonbattle.me/v2/trainers?trainer_id=2570'
    body = {
        "trainer_token": "a09e90a8051defb85956dd8b8753d6ca",
        "email": "ArtemyKonovalov.AK@yandex.ru",
        "password": "5310Kent"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(url, json=body, headers=headers)
    trainer_data = response.json()['data']
    assert any(trainer['trainer_name'] == 'Kent' for trainer in trainer_data), 'Нет проверяемой имени'