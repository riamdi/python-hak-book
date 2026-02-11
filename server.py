import socket
import threading

def handle_socket(client_soket, client_address):
    print(f'Connect to: {client_address}')
    client_soket.send(b'hello, client!')
    data = client_soket.recv(1024)
    print(f'Message client: {data.decode()}')
    client_soket.close()

def start_server():
    try:
        server_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_soket.bind(('localhost', 5000))
        server_soket.listen(5)
        print('Server online...')
        
        while True:
            client_soket, client_address = server_soket.accept()
            client_handler = threading.Thread(
                target=handle_socket,
                args=(client_soket, client_address)
            )
            client_handler.start()
    except OSError as e:
        print(f'Server erorr^ {e}')
    finally:
        server_soket.close()


if __name__ == '__main__':
    start_server()