import socket
import os
#1

# def client_start():
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.connect(('localhost', 5000))
#         print('Client online...')
#         client_socket.send(b'hello, server!')
#         data = client_socket.recv(1024)
#         print(f'Message server: {data.decode()}')
#     except OSError as e:
#         print(f'erorr: {e}')
#     finally:
#         client_socket.close()

#2
# def client_start():
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.connect(('localhost', 5000))
#         print('Client online...')
#         client_socket.send(b'2 15')
#         data = client_socket.recv(1024)
#         print(f'Message server: {data.decode()}')
#     except OSError as e:
#         print(f'erorr: {e}')
#     finally:
#         client_socket.close()

#3

# def client_start():
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.connect(('localhost', 5000))
#         print('Client online...')

#         file_size = os.path.getsize("file.txt")
#         message_size = str(file_size)
#         client_socket.send(message_size.encode())

#         data = client_socket.recv(1024)
#         print(f'Message from server: {data.decode()}')
#         with open('file.txt', 'r') as file:
#             content = file.read()
#             client_socket.send(content.encode())
#         message_server = client_socket.recv(1024)
#         print(f'Server to: {message_server.decode()}')
#     except OSError as e:
#         print(f'erorr: {e}')
#     finally:
#         client_socket.close()

#4

def client_start():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5000))
        print('Client online...')
        data = client_socket.recv(1024)
        print(f'Time now: {data.decode()}')
    except OSError as e:
        print(f'erorr: {e}')
    finally:
        client_socket.close()
if __name__ == '__main__':
    client_start()

