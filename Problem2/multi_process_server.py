import socket
import time
import multiprocessing
import signal
import sys

def handle_client(client_socket):
    """Handles a single client connection."""
    try:
        message = client_socket.recv(1024).decode()
        time.sleep(3)  # Simulate processing delay
        client_socket.sendall(message[::-1].encode())
    finally:
        client_socket.close()  # Ensure socket is closed

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(100)

    print("Multi-Process Server listening on", host, port)

    processes = []  # Track child processes

    # Handle server shutdown properly
    def shutdown_server(signum, frame):
        print("\nShutting down server...")
        for p in processes:
            p.terminate()
            p.join()
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_server)  # Handle Ctrl+C

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")
            process = multiprocessing.Process(target=handle_client, args=(client_socket,))
            process.start()
            processes.append(process)
            client_socket.close()  # Parent process closes its copy
    except Exception as e:
        print("Server error:", e)
    finally:
        shutdown_server(None, None)

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Required for Windows
    main()
