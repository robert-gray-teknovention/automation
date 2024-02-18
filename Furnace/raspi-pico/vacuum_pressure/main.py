from machine import Pin, ADC
from time import sleep
from wifi import WifiConnector
import network
import json
import urequests
import secrets
import gc
import uasyncio
import queue

vac_signal = ADC(Pin(26))
airflow_switch = Pin(22)
led = Pin('LED', Pin.OUT)
port = secrets.PORT
server_ip = secrets.IP
url = server_ip + port + '/apis/real_data_entries/'
headers = {'Content-Type': 'application/json'}

#Pressure monitor variables

value = 0
sample_size = 20
pause = 0.4
first_loop = True
    
def send_message(url, message):
    try:
        print(url)
        m = json.dumps(message)
        h = json.dumps(headers)
        print(m)
        r = urequests.post(url, data=m, headers=headers)
        print("Hey we just sent a request")
        print(r.status_code)
        gc.collect()
    except Exception as e:
        print(e)
            
async def filter(fan_on, signal, length=10, pause=0.5):
    lst = []
    while True:
        for n in range(length):
            signal_value = signal.read_u16()
            print("Signal ", signal_value)
            if len(lst) == length:
                lst.pop()
            lst.insert(0, signal_value)
            await uasyncio.sleep(pause)
        value = sum(lst)/len(lst)
        n=0

        if fan_on.value() == 1:
            #print("We are going to try and send a message")
            url = server_ip + port + '/apis/real_data_entries/'
            message = {
                'data_item': 1,
                'value': float(value),
                }
            send_message(url, message)
            led.value(1)
            await uasyncio.sleep_ms(500)
            led.value(0)
        print("\tAverage Value = ", value)
    
    
    

async def blink(led, delay):
    while True:
        led.toggle()
        await uasyncio.sleep(delay)

async def airflow():
    
    while True:
        prev = airflow_switch.value()
        while (prev == airflow_switch.value()):
            prev = airflow_switch.value()
            await uasyncio.sleep(0.04)
        print("Switch state changed ", airflow_switch.value())
        url = server_ip + port + '/apis/discrete_data_entries/'
        message = {
                'data_item': 2,
                'value': airflow_switch.value(),
                }
        send_message(url, message)
    

async def main():
    # q = queue.Queue()
    wifi = WifiConnector(secrets.SSID, secrets.PASSWORD)
    while not wifi.isconnected():
        print(secrets.SSID, secrets.PASSWORD)
        wifi.connect()
        sleep(2)
    uasyncio.create_task(airflow())
    #uasyncio.create_task(blink(led, 0.2))
    uasyncio.create_task(filter(airflow_switch, vac_signal, length=10, pause=0.5))
    while wifi.isconnected():
        print("We are running main loop")
        await uasyncio.sleep(2)
        
        
        '''
        '''
uasyncio.run(main())

