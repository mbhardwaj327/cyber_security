import socket

TARGET_HOST = '10.6.2.240'
TARGET_PORT = 12345

def start_session():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((TARGET_HOST, TARGET_PORT))

        first_input = input("Please enter your initial text: ").strip()
        first_packet = f"PKT1>>{first_input}"
        sock.sendall(first_packet.encode())
        response1 = sock.recv(1024).decode()
        print("Reply #1:", response1)

        second_input = input("Please enter your follow-up text: ").strip()
        second_packet = f"PKT2>>{second_input}"
        sock.sendall(second_packet.encode())
        response2 = sock.recv(1024).decode()
        print("Reply #2:", response2)

    except ConnectionRefusedError:
        print("Connection failed. Verify host and port.")
    except Exception as ex:
        print("Unexpected error:", ex)
    finally:
        sock.close()

if __name__ == "__main__":
    start_session()
