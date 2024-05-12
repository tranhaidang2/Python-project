import asyncio

writers = []

async def forward(addr, message):
    for writer in writers:
        if writer.get_extra_info('peername') != addr:
            writer.write(f"{addr}: {message}\n".encode())
            await writer.drain()

async def handle(reader, writer):
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    await forward(addr, message)
    writers.append(writer)
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            message = data.decode().strip()
            print(f"{addr}: {message}")  # In tin nhắn trên server
            await forward(addr, message)
            if message.lower() == "exit":
                break
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        writers.remove(writer)
        writer.close()

async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())
