import pytest
import socket
import asyncio
from .quic_base_client import send_quic_message

# TCP Test
def test_tcp_server():
    """
    Tests the TCP server by sending a message and checking the uppercase response.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 23456))
        message = "hello tcp"
        s.sendall(message.encode())
        data = s.recv(1024)
        assert data.decode() == message.upper()

# UDP Test
def test_udp_server():
    """
    Tests the UDP server by sending a message and checking the uppercase response.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = ("localhost", 12345)
        message = "hello udp"
        s.sendto(message.encode(), server_address)
        data, _ = s.recvfrom(1024)
        assert data.decode() == message.upper()

# QUIC Test
@pytest.mark.asyncio
async def test_quic_server():
    """
    Tests the QUIC server by sending a message and checking the uppercase response.
    """
    message = "hello quic"
    response = await send_quic_message("127.0.0.1", 4433, message)
    assert response == message.upper()
