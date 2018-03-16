import sys
import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl
import netifaces
import json


KEYFILE = 'key'
CERTFILE = 'cert'


LHOST = netifaces.ifaddresses('en0')[netifaces.AF_INET][0]['addr']      # MAC
# LHOST = netifaces.ifaddresses('eth1')[netifaces.AF_INET][0]['addr']   -> Kali
LPORT = 4444


def create_config_file_json():
    data = {
        'ip' : LHOST,
        'port' : LPORT
    }
    json_str = json.dumps(data)
    with open('config_w.json', 'w') as f:
        json.dump(data, f)
    f.close()


def get_json_data(json_file):
    return json.load(open(json_file))


def echo_client(s):
    while True:
        data = s.recv(8192)
        print(data.decode("utf-8"))
        if data == b'':
            break
        s.send(b'This is a response.')
        print('Connection closed')
    s.close()


def echo_server(address):
    s = socket.socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    s_ssl = ssl.wrap_socket(s, 
                            keyfile=KEYFILE,
                            certfile=CERTFILE, 
                            server_side=True)

    while True:
        try:
            (c,a) = s_ssl.accept()
            print('Got connection', a)
            while 1:
                c.write(str(input("Enter Something: ")).encode())
            # echo_client(c)
        except socket.error as e:
            print('Error: {0}'.format(e))


def main():
    create_config_file_json()
    config_data = get_json_data('config_w.json')
    echo_server((socket.gethostbyname(config_data['ip']), config_data['port']))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
            sys.exit(2)
