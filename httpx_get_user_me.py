import httpx

# Получаем токены пользователя
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)

print(f'Status code: {login_response.status_code}')
print(f'Login response: {login_response.json()}')
print()

# Запрашиваем данные пользователя используя токен
header = {'Authorization': f'Bearer {login_response.json()['token']['accessToken']}'}
users_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=header)

print(f'Status code: {users_response.status_code}')
print(f'User response: {users_response.json()}')
