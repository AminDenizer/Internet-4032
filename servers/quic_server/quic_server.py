import asyncio
from aioquic.asyncio import QuicConnectionProtocol, serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived

class UppercaseProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            data = event.data.decode()
            print(f"Received from client: {data}")
            response = data.upper().encode()
            self.send_stream_data(event.stream_id, response, end_stream=True)

async def main():
    configuration = QuicConfiguration(is_client=False)
    configuration.load_cert_chain("server.crt", "server.key")
    await serve(
        "0.0.0.0",
        4433,
        configuration=configuration,
        create_protocol=UppercaseProtocol,
    )
    print("QUIC server is up and listening on port 4433...")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
