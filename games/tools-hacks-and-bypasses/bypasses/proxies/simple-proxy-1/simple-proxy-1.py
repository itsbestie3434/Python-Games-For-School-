import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received request:\n{request.decode()}")

    # Extract the first line of the request
    first_line = request.split(b'\n')[0]
    url = first_line.split(b' ')[1]
    http_pos = url.find(b'://')  # Find the position of "://"
    if http_pos == -1:
        temp = url
    else:
        temp = url[(http_pos + 3):]  # Strip off the http:// or https://

    port_pos = temp.find(b':')  # Find the port if specified
    if port_pos == -1:
        port = 80  # Default port
        host = temp
    else:
        port = int(temp[(port_pos + 1):])  # Get the port number
        host = temp[:port_pos]  # Get the host name

    # Create a socket to connect to the target server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((host, port))
    server_socket.send(request)  # Send the request to the server

    while True:
        response = server_socket.recv(4096)  # Receive the response from the server
        if len(response) > 0:
            client_socket.send(response)  # Send the response back to the client
        else:
            break

    server_socket.close()
    client_socket.close()

def start_proxy(port=8888):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[*] Listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_proxy()
