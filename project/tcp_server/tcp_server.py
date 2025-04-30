# tcp_server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 23456)

server_socket.bind(server_address)
server_socket.listen(1)  # maximum parallel connection 
print("TCP server is up and listening...")

while True:
    connection, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    data = connection.recv(1024)
    if data:
        message = data.decode()
        print(f"Received from client: {message}")

        capitalized_message = message.upper()
        connection.sendall(capitalized_message.encode())

    connection.close()
