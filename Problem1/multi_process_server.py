import socket
import os
import multiprocessing

def handle_client(client_socket, addr):
    """Handle client requests in a new process."""
    process_id = os.getpid()  # Get process ID
    print(f"[Process {process_id}] Handling new client request from {addr}")

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

    print(f"[Process {process_id}] Closing connection")
    client_socket.close()

def main():
    server_host = "127.0.0.1"
    server_port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Multi-Process Server listening on {server_host}:{server_port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection from {addr}")

        # Create a new process for each client
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket, addr))
        client_process.start()
                
        print(f"Started process {client_process.pid} for client {addr}")

        # Close the parent copy of the client socket (to avoid resource leaks)
        client_socket.close()

if __name__ == "__main__":
    main()
