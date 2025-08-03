import socket
import asyncio

async def main():
    loop = asyncio.get_running_loop()
    addr_infos = await loop.getaddrinfo(
        "127.0.0.1",
        4433,
        type=socket.SOCK_DGRAM,
    )
    print(addr_infos)

if __name__ == "__main__":
    asyncio.run(main())
