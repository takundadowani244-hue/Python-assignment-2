## Question 3: Client-Server Program with Sockets##
import socket

def start_server(host="127.0.0.1", port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    print(f"Received message: {data.decode('utf-8')}")
                else:
                    print("No data received.")

    except OSError as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()
import socket

def start_client(host="127.0.0.1", port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            message = "Hello from client!"
            client_socket.sendall(message.encode("utf-8"))
            print(f"Sent: {message}")

    except ConnectionRefusedError:
        print("Connection failed: is the server running?")
    except OSError as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    start_client()