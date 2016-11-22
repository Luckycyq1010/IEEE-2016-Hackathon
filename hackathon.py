import sys, pygame, time, socket
from pygame.locals import *

pygame.init()
pygame.joystick.init()
jerry = pygame.joystick.Joystick(0)
jerry.init()
#print(pygame.joystick.get_count())
#print(jerry.get_numbuttons())
run = True
BUTTON0 = False
BUTTON1 = False
BUTTON2 = False
BUTTON3 = False
BUTTON4 = False
BUTTON5 = False
BUTTON6 = False
BUTTON7 = False
BUTTON8 = False
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('ieee.littlebencreations.com', 8089))


#x = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if jerry.get_button(0):
                BUTTON0 = True
            if jerry.get_button(1):
                BUTTON1 = True
            if jerry.get_button(2):
                BUTTON2 = True
            if jerry.get_button(3):
                BUTTON3 = True
            if jerry.get_button(4):
                BUTTON4 = True
            if jerry.get_button(5):
                BUTTON5 = True
            if jerry.get_button(6):
                BUTTON6 = True
            if jerry.get_button(7):
                BUTTON7 = True
            if jerry.get_button(8):
                BUTTON8 = True
            if jerry.get_button(9):
                run = False
        if event.type == pygame.JOYBUTTONUP:
            if not jerry.get_button(0):
                BUTTON0 = False
            if not jerry.get_button(1):
                BUTTON1 = False
            if not jerry.get_button(2):
                BUTTON2 = False
            if not jerry.get_button(3):
                BUTTON3 = False
            if not jerry.get_button(4):
                BUTTON4 = False
            if not jerry.get_button(5):
                BUTTON5 = False
            if not jerry.get_button(6):
                BUTTON6 = False
            if not jerry.get_button(7):
                BUTTON7 = False
            if not jerry.get_button(8):
                BUTTON8 = False
            if not jerry.get_button(9):
                BUTTON9 = False
        send = str(BUTTON0)[:1] + str(BUTTON1)[:1] + str(BUTTON2)[:1] + str(BUTTON3)[:1] + str(BUTTON4)[:1] + str(BUTTON5)[:1] + \
               str(BUTTON6)[:1] + str(BUTTON7)[:1] + str(BUTTON8)[:1]
        clientsocket.send(send)
