import socket


def server(response=[]):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(10)

    server_socket.settimeout(1.0)

    print("Сервер запущен и ждет подключений...")

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
            except socket.timeout:
                continue

            print(f"Пользователь с адресом: {client_address} подключился к серверу")

            data = client_socket.recv(1024).decode()
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

            response.append(data)
            client_socket.send('\n'.join(response).encode())

            client_socket.close()

    except KeyboardInterrupt:
        print("Сервер остановлен")

    finally:
        server_socket.close()


if __name__ == "__main__":
    server()
