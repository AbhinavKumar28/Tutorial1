import socket

def process_request(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data or data.startswith("4"):
            print("Client disconnected.")
            break

        choice, value = data.split(":", 1)

        if choice == "1":
            response = value.swapcase()
        elif choice == "2":
            try:
                response = str(eval(value))
            except Exception as e:
                response = f"Error: {str(e)}"
        elif choice == "3":
            response = value[::-1]
        else:
            response = "Invalid option."

        client_socket.sendall(response.encode())

    client_socket.close()

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    
    print("Single-Process Server is running...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection established with {client_addr}")
        process_request(client_socket)

if __name__ == "__main__":
    main()
