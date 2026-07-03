from httpx import Client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.authentication.authentication_client import get_authentication_client
from clients.event_hooks import curl_event_hook
from pydantic import BaseModel
from config import settings
from functools import lru_cache


class AuthenticationUserSchema(BaseModel, frozen=True):
    """
    Описание структуры данных пользователя для авторизации.
    """
    email: str
    password: str


@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    authentification_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentification_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )
