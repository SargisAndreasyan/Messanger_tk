import socket
from threading import Thread
PORT = 9090
ADDRESS = '127.0.0.1'

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((ADDRESS,PORT))

def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode('utf-8'),'\n')

def send_server():
    listen_thread = Thread(target=listen_server)
    listen_thread.start()
    while True:
        client.send(input("Enter msg\n").encode('utf-8'))

if __name__ == "__main__":
    send_server()