import socket
import threading

SERVER_ADDRESS = '10.6.2.240'
SERVER_PORT = 12345

def transform_payload(payload):
    return payload.upper()

def connection_worker(client_sock, client_addr, client_id):
    with client_sock:
        print(f"{client_addr} connected as client {client_id}")
        while True:
            chunk = client_sock.recv(1024)
            if not chunk:
                break
            text = chunk.decode().strip()
            print(f"{client_addr} -> {text!r}")
            reply = transform_payload(text)
            client_sock.sendall(reply.encode())
            print(f"{client_addr} <- {reply!r}")

            chunk = client_sock.recv(1024)
            if not chunk:
                break
            text = chunk.decode().strip()
            print(f"{client_addr} -> {text!r}")
            reply = transform_payload(text)
            client_sock.sendall(reply.encode())
            print(f"{client_addr} <- {reply!r}")

        print(f"{client_addr} disconnected")

def launch_server():
    client_count = 0
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((SERVER_ADDRESS, SERVER_PORT))
    listener.listen()
    print(f"Listening on {SERVER_ADDRESS}:{SERVER_PORT}")
    try:
        while True:
            conn, addr = listener.accept()
            client_count += 1
            thread = threading.Thread(
                target=connection_worker,
                args=(conn, addr, client_count),
                daemon=True
            )
            thread.start()
    except KeyboardInterrupt:
        print("Server shutdown initiated")
    finally:
        listener.close()

if __name__ == "__main__":
    launch_server()
