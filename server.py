import socket

# host and port declaration
HOST, PORT = 'localhost', 8080

# socket declaration
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is the internet address family for IPv4, SOCK_STREAM is the socket type for TCP
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SOL_SOCKET is the socket layer itself, used for options that are protocol independant. 
listen_socket.bind((HOST, PORT)) # SO_REUSEADDR is the option enable addresses to be reused. generally a good thing but can lead to security vulnerabilities and data corruption.
listen_socket.listen(1) # starts listening for incoming connections
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept() # accepts a connection from a client and returns a new socket for communication
    request_data = client_connection.recv(1024) # 1024 bytes of data can be received
    print(request_data.decode('utf-8')) # decodes and prints data

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
""" # using b"""\ to turn message into bytes to send, message is in POST format
    client_connection.sendall(http_response) # sends response
    client_connection.close() # closes connection