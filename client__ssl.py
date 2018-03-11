import ssl

port = 8082

import socket, ssl

def echo_client(s):
    while True:
        data = s.recv(8192)
        print(data.decode("utf-8"))
        if data == 'ola':
            print('niceee')
        if data == b'':
            break
        s.send(b'This is a response.')
        print('Connection closed')
    s.close()

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Require a certificate from the server. We used a self-signed certificate
    # so here ca_certs must be the server certificate itself.
    ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED, ca_certs='cert')

    ssl_sock.connect(('127.0.0.1', 8087))

    echo_client(ssl_sock)


    

    ssl_sock.close()
