import socket
import time
import threading
import signal
import sys

def handle_client(client_socket):
    """Handles a single client connection."""
    thread_name = threading.current_thread().name
    print(f"Handling client in {thread_name}")
    
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

    print("Multi-Threaded Server listening on", host, port)

    threads = []  # Track threads

    # Handle server shutdown properly
    def shutdown_server(signum, frame):
        print("\nShutting down server...")
        for thread in threads:
            thread.join()  # Wait for threads to complete
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_server)  # Handle Ctrl+C

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
            threads.append(thread)
    except Exception as e:
        print("Server error:", e)
    finally:
        shutdown_server(None, None)

if __name__ == "__main__":
    main()
