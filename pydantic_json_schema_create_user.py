from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from clients.users.private_users_client import get_users_client

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_users_client(authentication_user)

get_users_response = private_users_client.get_user_api(create_user_response_json['user']['id'])
get_users_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_users_response.json(), schema=get_users_response_schema)
