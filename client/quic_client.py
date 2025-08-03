import asyncio
from client.quic_base_client import send_quic_message

async def main():
    message = "hello from quic client"
    response = await send_quic_message("127.0.0.1", 4433, message)
    print("Received from server:", response)

if __name__ == "__main__":
    asyncio.run(main())
