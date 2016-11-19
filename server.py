import socket
from threading import *
'''serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
connection, address = serversocket.accept()
while True:
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf.decode())
        break'''

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "155.246.207.22"
port = 8089
print (host)
print (port)
#serversocket.bind((host, port))
serversocket.bind(("", 8089))
#value = 'FFFFFFFFF'
BUTTON0 = False
BUTTON1 = False
BUTTON2 = False
BUTTON3 = False
BUTTON4 = False
BUTTON5 = False
BUTTON6 = False
BUTTON7 = False
BUTTON8 = False


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            value = self.sock.recv(1024).decode()
            print(value)

            if value[0] == 'T':
                BUTTON0 = True
            if value[0] == 'F':
                BUTTON0 = False
            if value[1] == 'T':
                BUTTON1 = True
            if value[1] == 'F':
                BUTTON1 = False
            if value[2] == 'T':
                BUTTON2 = True
            if value[2] == 'F':
                BUTTON2 = False
            if value[3] == 'T':
                BUTTON3 = True
            if value[3] == 'F':
                BUTTON3 = False
            if value[4] == 'T':
                BUTTON4 = True
            if value[4] == 'F':
                BUTTON4 = False
            if value[5] == 'T':
                BUTTON5 = True
            if value[5] == 'F':
                BUTTON5 = False
            if value[6] == 'T':
                BUTTON6 = True
            if value[6] == 'F':
                BUTTON6 = False
            if value[7] == 'T':
                BUTTON7 = True
            if value[7] == 'F':
                BUTTON7 = False
            if value[8] == 'T':
                BUTTON8 = True
            if value[8] == 'F':
                BUTTON8 = False
            self.sock.send(b'Oi you sent something to me')

            print(BUTTON2)


serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
