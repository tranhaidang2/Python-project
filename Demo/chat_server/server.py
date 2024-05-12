import asyncio
import errno
import time

host = "127.0.0.1"
port = 9000

async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    addr, port = writer.get_extra_info("peername")
    print(f"New connection from {addr}:{port}:")

    while True:
        data = await reader.readline()
        if not data:
            break
        
        message = data.decode().strip()
        print(f"Message from {addr}:{port}: {message!r}")

        if message == "quit":
            print(f"Closing connection from {addr}:{port}")
            writer.close()
            await writer.wait_closed()
            break
        else:
            writer.write(data)
            await writer.drain()
async def run_server() -> None:
    try:
        server = await asyncio.start_server(handle_echo, host, port)
        print(f"Server started and listening on {host}:{port}")

        try:
            while True:
                await asyncio.sleep(2)
        except KeyboardInterrupt:
            print("Server shutting down...")
            server.close()
            await server.wait_closed()
        except asyncio.CancelledError:
            pass
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print(f"Port {port} is already in use. Please choose another port.")
        else:
            raise

if __name__ == "__main__":
    asyncio.run(run_server())

'''

    Để chạy được chường trình ta tiến hành các bước sau:
    B1: Chạy file Server
    B2: Chạy file Client, nếu chạy file Client mà chưa chạy fill Server thì sẽ không thể kết nối

    Nhấn Ctrl + C để tắt Server
'''

