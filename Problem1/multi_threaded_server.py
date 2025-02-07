import socket
import threading

def handle_client(client_socket):
    """Handle client requests in a new thread."""
    thread_name = threading.current_thread().name  # Get thread name

    print(f"[{thread_name}] Handling new client request")

    while True:
        task = client_socket.recv(1024).decode()
        if not task or task.lower() == "exit":
            break
        elif task.startswith("1"):  # Change case
            response = task[2:].swapcase()
        elif task.startswith("2"):  # Evaluate expression
            try:
                response = str(eval(task[2:]))
            except Exception:
                response = "Error in expression"
        elif task.startswith("3"):  # Reverse string
            response = task[2:][::-1]
        else:
            response = "Invalid option"
        
        client_socket.send(response.encode())

    print(f"[{thread_name}] Closing connection")
    client_socket.close()

def main():
    server_host = "127.0.0.1"
    server_port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Multi-Threaded Server listening on {server_host}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")

        # Create a new thread for each client and name it uniquely
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

        print(f"Started thread {client_thread.name} for client {addr}")

if __name__ == "__main__":
    main()
