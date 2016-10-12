#!/user/bin/env python

import socket
from httprequest import HTTPRequest


HOST, PORT = '', 5000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port %s... ' % PORT)

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)
    print('')
    http_request = HTTPRequest(request)
    print('method:', http_request.method)
    print('')
    client_connection.sendall(request)
    client_connection.close()

