import asyncio
import signal
import time

host = "127.0.0.1"
port = 9000

async def run_client(client_id):
    writer = None
    try:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"Connected to the server from Client {client_id}")

        for _ in range(3):
            message = f"Client {client_id}: Message {_ + 1}"
            writer.write(message.encode() + b"\n")
            await writer.drain()

            data = await reader.read(1024)
            print(f"Server response to Client {client_id}: {data.decode()!r}")

        writer.write(b"quit")
        await writer.drain()

    except Exception:
        print(f"Failed to connect to the server from Client {client_id}")
    finally:
        if writer and not writer.transport.is_closing():
            writer.close()
            await writer.wait_closed()

async def main():
    tasks = []
    for i in range(10):
        task = asyncio.create_task(run_client(i))
        tasks.append(task)
    await asyncio.gather(*tasks)

def signal_handler(signalnum, frame):
    print("Exiting...")
    raise KeyboardInterrupt

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
