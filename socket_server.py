import socket
import threading

def handler_client(client_socket, client_address):
            print(f'Server connect with: {client_address}')
            client_socket.send(b'hello, client!')
            data = client_socket.recv(1024)
            print(f'Client say: {data.decode()}')
            client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 5000))
        server_socket.listen(5)
        print('Server online')

        while True:
            client_socket, client_address = server_socket.accept()
            client_handler = threading.Thread(
                 target=handler_client,
                 args=(client_socket, client_address)
            )
            client_handler.start()

    except OSError as e:
        print(f'Ошибка сервера: {e}')
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
