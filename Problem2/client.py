import socket

def main():
    host = "127.0.0.1"  # Server IP
    port = 12345  # Must match the server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = "Hello, Server"
    client_socket.sendall(message.encode())  # Send message
    response = client_socket.recv(1024).decode()  # Receive response
    print(f"Received: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
