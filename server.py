import socket
from threading import *
import roomba

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
#serversocket.bind((host, port))
serversocket.bind(("", 8089))
#value = 'FFFFFFFFF'
BUTTON0 = False # Left
BUTTON1 = False # Down
BUTTON2 = False #
BUTTON3 = False #
BUTTON4 = False #
BUTTON5 = False #
BUTTON6 = False #
BUTTON7 = False #
BUTTON8 = False #


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
                buttonChanged(0, True)
            if value[0] == 'F':
                BUTTON0 = False
                buttonChanged(0, False)
            if value[1] == 'T':
                BUTTON1 = True
                buttonChanged(1, True)
            if value[1] == 'F':
                BUTTON1 = False
                buttonChanged(1, False)
            if value[2] == 'T':
                BUTTON2 = True
                buttonChanged(2, True)
            if value[2] == 'F':
                BUTTON2 = False
                buttonChanged(2, False)
            if value[3] == 'T':
                BUTTON3 = True
                buttonChanged(3, True)
            if value[3] == 'F':
                BUTTON3 = False
                buttonChanged(3, False)
            if value[4] == 'T':
                BUTTON4 = True
                buttonChanged(4, True)
            if value[4] == 'F':
                BUTTON4 = False
                buttonChanged(4, False)
            if value[5] == 'T':
                BUTTON5 = True
                buttonChanged(5, True)
            if value[5] == 'F':
                BUTTON5 = False
                buttonChanged(5, False)
            if value[6] == 'T':
                BUTTON6 = True
                buttonChanged(6, True)
            if value[6] == 'F':
                BUTTON6 = False
                buttonChanged(6, False)
            if value[7] == 'T':
                BUTTON7 = True
                buttonChanged(7, True)
            if value[7] == 'F':
                BUTTON7 = False
                buttonChanged(7, False)
            if value[8] == 'T':
                BUTTON8 = True
                buttonChanged(8, True)
            if value[8] == 'F':
                BUTTON8 = False
                buttonChanged(8, False)

            cond = False
            for val in value:
                if val == 'T':
                    cond = True
            if cond == False:
                roomba.stop()

            print(cond)

            self.sock.send(b'Oi you sent something to me')


TURNSPEED = 200
DRIVESPEED = 200

motors = [False, False, False]


def buttonChanged(button, value):
    if button == 2:
        if value:
            roomba.drive(DRIVESPEED,0)
            print("forward")
    elif button == 3:
        if value:
            roomba.drive(TURNSPEED, -1)
            print("left")
    elif button == 0:
        if value:
            roomba.drive(TURNSPEED, 1)
            print("right")
    elif button == 1:
        if value:
            roomba.drive(-DRIVESPEED, 0)
            print("backward")
    elif button == 6:
        if value:
            motors[0] = not motors[0]
            roomba.motor2(motors[0], motors[1], motors[2])
    elif button == 7:
        if value:
            motors[1] = not motors[1]
            roomba.motor2(motors[0], motors[1], motors[2])
    elif button == 5:
        if value:
            motors[2] = not motors[2]
            roomba.motor2(motors[0], motors[1], motors[2])

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
