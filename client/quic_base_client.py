import asyncio
import ssl
from aioquic.quic.configuration import QuicConfiguration
from .fixed_aioquic import connect

async def send_quic_message(host: str, port: int, message: str) -> str:
    """
    Connects to a QUIC server, sends a message, and returns the response.
    """
    configuration = QuicConfiguration(is_client=True, alpn_protocols=["hq-29"])
    configuration.verify_mode = ssl.CERT_NONE

    async with connect(host, port, configuration=configuration) as client:
        reader, writer = await client.create_stream()
        writer.write(message.encode())
        writer.write_eof()
        response = await reader.read()
        return response.decode()
