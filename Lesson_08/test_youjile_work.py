import requests
from config import TOKEN

TOKEN

URL = 'https://ru.yougile.com'

HEADERS = {'Authorization': f"Bearer {TOKEN}", 'Content-Type': 'application/json'}


def test_create_project_positive():

    '''Позитивный тест создания проекта'''

    body = {"title": "Проект урок 8.1",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}
    responce = requests.post(url=f'{URL}/api-v2/projects', json=body, headers=HEADERS)

    assert responce.status_code == 201

    responce_body = responce.json()

    id = responce_body['id']

    body = {"deleted": True}

    responce = requests.put(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    assert responce.status_code == 200


def test_create_project_negative():

    '''Негативный тест создания проекта'''

    body = {"title": "",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}
    responce = requests.post(url=f'{URL}/api-v2/projects', json=body, headers=HEADERS)

    assert responce.status_code == 400


def test_edit_project_positive():

    '''Позитивный тест редактирования проекта'''

    body = {"title": "Проект урок 8.2",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}
    responce = requests.post(url=f'{URL}/api-v2/projects', json=body, headers=HEADERS)

    assert responce.status_code == 201

    responce_body = responce.json()

    id = responce_body['id']

    body = {"title": "Знакомство с библиотекой Requests",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}

    responce = requests.put(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    assert responce.status_code == 200

    responce_body = responce.json()

    id = responce_body['id']

    body = {"deleted": True}

    responce = requests.put(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    assert responce.status_code == 200


def test_edit_project_negative():

    '''Негативный тест редактирования проекта'''

    body = {"title": "Проект урок 8.3",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}
    responce = requests.post(url=f'{URL}/api-v2/projects', json=body, headers=HEADERS)

    assert responce.status_code == 201

    responce_body = responce.json()

    id = responce_body['id']

    body = {"title": "",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}

    responce = requests.put(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    print(responce)

    assert responce.status_code == 400


def test_get_project_with_id_positive():

    '''Позитивный тест получения проекта по id'''

    body = {"title": "Проект урок 8.4",
            "users": {"4be9cbc1-7706-41a0-a9e1-0f1240006894": "admin"}}

    responce = requests.post(url=f'{URL}/api-v2/projects', json=body, headers=HEADERS)

    assert responce.status_code == 201

    responce_body = responce.json()

    id = responce_body['id']

    responce = requests.get(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    assert responce.status_code == 200

    body = {"deleted": True}

    responce = requests.put(url=f'{URL}/api-v2/projects/{id}', json=body, headers=HEADERS)

    assert responce.status_code == 200


def test_get_project_with_id_negative():

    '''Негативный тест получения проекта по id'''

    id = 33333333333333333

    responce = requests.get(url=f'{URL}/api-v2/projects/{id}', headers=HEADERS)

    assert responce.status_code == 404
