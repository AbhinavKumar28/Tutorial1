import socket

def main():
    server_host = "127.0.0.1"
    server_port = 12345  # Ensure this matches the server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    while True:
        print("\nMenu:")
        print("1. Change the case of a string")
        print("2. Evaluate a mathematical expression")
        print("3. Find the reverse of a string")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "4":
            client_socket.sendall(choice.encode())
            print("Exiting...")
            break

        if choice in ("1", "2", "3"):
            data = input("Enter input data: ")
            message = f"{choice}:{data}"
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024).decode()
            print(f"Server Response: {response}")
        else:
            print("Invalid choice. Try again.")

    client_socket.close()

if __name__ == "__main__":
    main()
