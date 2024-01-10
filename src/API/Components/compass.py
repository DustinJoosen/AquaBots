import smbus
import grove_compass_lib

def get_compass():
    c=grove_compass_lib.compass()

    adres = 0x08
    register = 0x00

    bus = smbus.SMBus(1)
    
    return c.headingDegrees
