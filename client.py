import socket

def client_start():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 5000))
        print('Client online...')

        data = client_socket.recv(1024)
        client_socket.send(b'hello, server 2!')
        print(f'Message server: {data.decode()}')
    except OSError as e:
        print(f'erorr: {e}')
    finally:
        client_socket.close()

if __name__ == '__main__':
    client_start()

