import asyncio
import ssl
from client.fixed_aioquic import connect
from aioquic.quic.configuration import QuicConfiguration


async def run_quic_client(host, port, message):
    configuration = QuicConfiguration(is_client=True, alpn_protocols=["hq-29"])
    configuration.verify_mode = ssl.CERT_NONE

    async with connect(host, port, configuration=configuration) as client:
        # create a stream
        stream_id = client._quic.get_next_available_stream_id(is_unidirectional=False)
        client._quic.send_stream_data(stream_id, message.encode(), end_stream=True)

        # receive the response
        reader = client._stream_readers[stream_id]
        response = await reader.read()
        print("Received from server:", response.decode())


if __name__ == "__main__":
    asyncio.run(run_quic_client("127.0.0.1", 4433, "hello from quic client"))
