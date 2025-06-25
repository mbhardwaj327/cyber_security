import socket

SERVER_IP = '10.6.2.240'
SERVER_PORT = 12345

def communicate_with_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))

        user_input1 = input("Type your first message: ").strip()
        formatted_msg1 = f"MSG01::{user_input1}"
        client_socket.sendall(formatted_msg1.encode())
        reply1 = client_socket.recv(1024)
        print("Received from server:", reply1.decode())

        user_input2 = input("Type your second message: ").strip()
        formatted_msg2 = f"MSG02::{user_input2}"
        client_socket.sendall(formatted_msg2.encode())
        reply2 = client_socket.recv(1024)
        print("Final response:", reply2.decode())

    except ConnectionRefusedError:
        print("Could not connect to the server. Please check the server address and port.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    communicate_with_server()
