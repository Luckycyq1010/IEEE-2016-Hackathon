import serial, time

ser = serial.Serial("/dev/tty.usbserial-AI04YQHA", baudrate=57600, timeout=0.1)



START = chr(128)

CONTROL = chr(130)

SAFE = chr(131)
FULL = chr(132)
POWER = chr(133) # turn off
SPOT = chr(134)
CLEAN = chr(135)
MAX = chr(135)
DRIVE = chr(137)


def drive(speed, radius):

    ser.send(START)
    #ser.send()


MOTORS = chr(138)


def motor2(main, vaccum, side): # all booleans

    m = (0b00000100 if main else 0)
    v = (0b00000010 if vaccum else 0)
    s = (0b00000001 if side else 0)

    total = m | v | s

    ser.write(START)
    ser.write(CONTROL)
    ser.write(MOTORS)
    ser.write(chr(total))


    return chr(total)



def fullMode():
    ser.write(START)
    ser.write(CONTROL)
    ser.write(FULL)
    time.sleep(0.2)


def safeMode():
    ser.write(START)
    ser.write(CONTROL)
    ser.write(SAFE)
    time.sleep(0.2)



def turnOn():
    for i in range(3):
        ser.setRTS(0)
        time.sleep(0.25)
        ser.setRTS(1)
        time.sleep(0.25)

def turnOff():
    ser.write(POWER)


def twosCompliment(number):
    highByte = number / 256

    if highByte < 0:
        highByte *= -1
        highByte = highByte ^ 0xFF
        highByte += 1


    return highByte, number % 256



def drive(speed, radius):
    ser.write(START)
    ser.write(CONTROL)
    ser.write(DRIVE)

    ser.write(chr(twosCompliment(speed)[0]))
    ser.write(chr(twosCompliment(speed)[1]))


    if radius == 0:
        ser.write(chr(0x80))
        ser.write(chr(0x00))
    else:
        ser.write(chr(twosCompliment(radius)[0]))
        ser.write(chr(twosCompliment(radius)[1]))





