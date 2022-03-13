import socket
import threading

PORT = 9090
ADDRESS = '127.0.0.1'

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((ADDRESS, PORT))

server.listen(5)
print("Server is listening!!!")
users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user):
    print("Listening user")
    while True:
        data = user.recv(2048)
        print(data)
        send_all(data)


def start_server():
    while True:
        user_socket, address = server.accept()
        user_socket.send(f"{address[0]} are connected!!!".encode('utf-8'))
        users.append(user_socket)
        listen_accepted_user = threading.Thread(
            target=listen_user,
            args= (user_socket,)
        )
        listen_accepted_user.start()

if __name__ == '__main__':
    start_server()
