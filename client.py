import socket

def main():
    host = "10.0.0.91"    #"server_ip_address"  # Replace with the server's IP address or hostname
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Server responded: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()

