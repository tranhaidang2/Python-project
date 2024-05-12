import asyncio
import signal

host = "127.0.0.1"
port = 8001

async def run_client() -> None:
    writer = None  # Khởi tạo writer với giá trị None

    try:
        reader, writer = await asyncio.open_connection(host, port)
        print("Connected to the server")

        while True:
            try:
                message = input("Enter message (type 'quit' to exit): ")
            except EOFError:
                break

            if message == 'quit':
                break

            writer.write(message.encode() + b"\n")
            await writer.drain()

            data = await reader.read(1024)
            print(f"Server response: {data.decode()!r}")

        writer.write(b"quit")
        await writer.drain()

    except Exception:
        print(f"Failed to connect to the server")
    finally:
        if writer and not writer.transport.is_closing():
            writer.close()
            await writer.wait_closed()

def signal_handler(signalnum, frame):
    print("Exiting...")
    raise KeyboardInterrupt

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    try:
        asyncio.run(run_client())
    except KeyboardInterrupt:
        print("Exiting...")