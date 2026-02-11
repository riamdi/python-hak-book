import socket

def client_start():
    socet_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socet_client.connect(('localhost', 5000))
    print('Client online')


    data = socet_client.recv(1024)
    print(f'Server say: {data.decode()}')
    socet_client.send(b'hello, server')
    socet_client.close()

if __name__ == '__main__':
    client_start()
