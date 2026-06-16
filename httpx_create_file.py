import httpx
from tools.fakers import get_random_email

# Создание пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print(create_user_response.status_code)
print(f'Create user: {create_user_response_data}')
print()

# Аутентификация пользователя
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(f'Authentication user: {login_response_data}')
print()

# Загрузка файла
create_file_header = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}",
}
create_file_response = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open("./testdata/files/image.png", "rb")},
    headers=create_file_header)
create_file_response_data = create_file_response.json()

print(create_file_response.status_code)
print(f'Create file: {create_file_response_data}')
print()
