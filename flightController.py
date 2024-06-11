from smbus import SMBus
import time
import serial
import pynmea2

i2c_address = 0x08
i2c_cmd_write = 0x01
i2c_cmd_read = 0x02

gps = serial.Serial("/dev/serial0", baudrate=9600, timeout=0.5)

bus = SMBus(1)

def sendPIDInputsOverI2C(roll, pitch, throttle):
    
    sendString = 'R '+ roll +' P '+ pitch +' T '+ throttle + '  '
    bus.write_i2c_block_data(i2c_address, i2c_cmd_write, convertStringToByte(sendString))
    print(sendString)

def sendHeadingToFly(heading):

    sendString = 'H '+ heading
    bus.write_i2c_block_data(i2c_address, i2c_cmd_write, convertStringToByte(sendString))
    print(sendString)

def convertStringToByte(src):
    converted = []
    for i in src:
        converted.append(ord(i))
    return converted

def getAltitude():
    bus.write_i2c_block_data(i2c_address, i2c_cmd_write, convertStringToByte("A  "))

    altitude = 0

    pressure = bus.read_i2c_block_data(i2c_address,  0x02, 16)

    print(pressure)

def getCoords():

    gpsString = gps.readline().decode().strip()

    if gpsString.find('GGA') > 0:
        msg = pynmea2.parse(gpsString)

        print('Lat: ', round(msg.latitude,6), 'Lng: ', round(msg.longitude,6), 'Altitude: ', round(msg.altitude))

        return (msg.latitude, msg.longitude)

def calculateHeadingToCoordinate(coordinate):

    pass


def takeOff():

    sendPIDInputsOverI2C('+00','+10','1100')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1200')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1300')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1400')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1500')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1600')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1700')
    time.sleep(1)
    sendPIDInputsOverI2C('+00','+10','1800')
    time.sleep(1)

sendHeadingToFly('100')
    



