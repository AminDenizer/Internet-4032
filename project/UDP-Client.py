# udp_client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('0.0.0.0', 12345)

message = input("Enter your message: ")
client_socket.sendto(message.encode(), server_address)

data, _ = client_socket.recvfrom(1024)
print("Received from server:", data.decode())

client_socket.close()
