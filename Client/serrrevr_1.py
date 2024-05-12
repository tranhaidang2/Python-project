import asyncio

async def receive_message(reader):
    while True:
        data = await reader.read(100)
        if not data:
            break
        print(data.decode(), end='')

async def send_message(writer):
    while True:
        message = input()
        writer.write(message.encode())
        await writer.drain()
        if message.lower() == "exit":
            break

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("Connected to server. You can start typing messages.")
    try:
        await asyncio.gather(receive_message(reader), send_message(writer), return_exceptions=True)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Closing connection...")
    finally:
        writer.close()
        await writer.wait_closed()

asyncio.run(main())

