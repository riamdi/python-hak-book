import socket
import threading
import datetime
#1
# def handle_socket(client_socket, client_address):
#     print(f'Connect to: {client_address}')
#     data = client_socket.recv(1024)
#     print(f'Message client: {data.decode()}')
#     new_message = data.decode().upper()
#     client_socket.send(new_message.encode())
#     print(f'My message: {new_message}')
#     client_socket.close()

#2
# def handle_socket(client_socket, client_address):
#     print(f'Connect to: {client_address}')
#     data = client_socket.recv(1024)
#     print(f'Message client: {data.decode()}')
#     result = int(data.split()[0]) + int(data.split()[1])
#     client_socket.send(str(result).encode())
#     print(f'My message: {result}')
#     client_socket.close()

# #3
# def handle_socket(client_socket, client_address):
#     print(f'Connect to: {client_address}')
#     message_size = int(client_socket.recv(1024).decode())
#     print(f'Message size: {message_size}')
#     client_socket.send(f'Server get size file: {message_size}'.encode())
#     if message_size > 1024:
#         file = client_socket.recv(message_size)
#     else:
#         file = client_socket.recv(1024)
#     print(f'Server get: {file.decode()}')
#     client_socket.send(f'Server get file from client.'.encode())
#     client_socket.close()

##4
# def handle_socket(client_socket, client_address):
#     print(f'Connect to: {client_address}')
#     data = datetime.datetime.now()
#     client_socket.send(str(data.time()).encode())
#     client_socket.close()

#5
def handle_socket(client_socket, client_address):
    print(f'Connect to: {client_address}')
    data = datetime.datetime.now()
    client_socket.send(str(data.time()).encode())
    client_socket.close()
def start_server():
    try:
        server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_soket.bind(('localhost', 5000))
        server_soket.listen(5)
        print('Server online...')
        
        while True:
            client_socket, client_address = server_soket.accept()
            client_handler = threading.Thread(
                target=handle_socket,
                args=(client_socket, client_address)
            )
            client_handler.start()
    except OSError as e:
        print(f'Server error: {e}')
    finally:
        server_soket.close()


if __name__ == '__main__':
    start_server()