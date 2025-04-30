# udp_server.py
import socket

# Creat UDP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

# Connect to ip and port 
server_socket.bind(server_address)
print("UDP server is up and listening...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Received from client: {message}")
    
    capitalized_message = message.upper()
    server_socket.sendto(capitalized_message.encode(), client_address)
