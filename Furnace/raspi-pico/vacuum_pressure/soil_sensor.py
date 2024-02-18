import machine
import time
from stemma_soil_sensor import StemmaSoilSensor as SSS
sdaPIN=machine.Pin(0)
sclPIN=machine.Pin(1)
i2c=machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
devices = i2c.scan()
if len(devices) != 0:
    print('Number of I2C devices found=',len(devices))
    for device in devices:
        print("Device Hexadecimel Address= ",hex(device))
else:
    print("No device found")

sss=SSS(i2c)
while True:
    for dev in devices:
        sss.addr = dev
        temp = sss.get_temp()
        print("Temperature of ", hex(sss.addr), " = ", temp)
        moisture = sss.get_moisture()
        time.sleep(.5)
        print("Moisture of ", hex(sss.addr), " = ", moisture)
        
    time.sleep(5)
        
