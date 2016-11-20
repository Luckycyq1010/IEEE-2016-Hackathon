'''
DEPRECIATED
Created on Nov 19, 2016

@author: evanlewis
'''
import socket, time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
message = "Hello"
#clientsocket.send(message.encode())
x = 0
while x < 500:
    x += 1
    time.sleep(1)
    clientsocket.send(message.encode())
