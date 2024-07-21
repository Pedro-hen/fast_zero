from http import HTTPStatus


def test_read_root_dev_retornar_ok_e_olar_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(  # validando o UserSchema
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password',
        },
    )

    # validando UsePublic
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testusername',
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'test2',
            'email': 'test@test.com',
            'password': '123',
        },
    )

    assert response.json() == {
        'id': 1,
        'username': 'test2',
        'email': 'test@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted!'}
