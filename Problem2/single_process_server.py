import socket
import time

def handle_client(client_socket):
    message = client_socket.recv(1024).decode()
    time.sleep(3)  # 3-second processing delay
    client_socket.sendall(message[::-1].encode())  # Reverse and send
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(100)

    print("Single-Process Server listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
