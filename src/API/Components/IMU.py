import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import smbus

class IMU:

    def __init__(self, bus: int, address: int):
        self.bus = bus
        self.address = address

        self.mpu = MPU9250(
            address_ak=AK8963_ADDRESS,
            address_mpu_master=address,
            address_mpu_slave=None,
            bus=bus,
            gfs=GFS_1000,
            afs=AFS_8G,
            mfs=AK8963_BIT_16,
            mode=AK8963_MODE_C100HZ,
        )
        self.mpu.configure()

    def read_data(self):
        return {
            "accelerometer": self.mpu.readAccelerometerMaster(),
            "gyroscope": self.mpu.readGyroscopeMaster(),
            "magnetometer": self.mpu.readMagnetometerMaster(),
        }

    def read_byte(self, register: int):
        return smbus.read_byte_data(self.address, register)



def get_accelerometer():
    imu = IMU(bus=1, address=0x68)
    data = imu.read_data()
    
    return data["accelerometer"]


def get_magnetometer():
    imu = IMU(bus=1, address=0x68)
    data = imu.read_data()
    
    return data["magnetometer"]


def get_gyroscope():
    imu = IMU(bus=1, address=0x68)
    data = imu.read_data()
    
    return data["gyroscope"]

