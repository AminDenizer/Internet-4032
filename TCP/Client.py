# tcp_client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)

client_socket.connect(server_address)
message = input("Enter your message: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print("Received from server:", data.decode())

client_socket.close()
