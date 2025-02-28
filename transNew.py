import serial
import json
import time
import RPi.GPIO as GPIO
from time import sleep
import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Button = 23
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

ser = serial.Serial('/dev/serial0', 9600, timeout=1)
i =0

while True:
    
    try:
        button_state = GPIO.input(Button)
        time.sleep(0.05)  # Wait for debounce time
        if button_state == GPIO.input(Button):  # Confirm the state after debounce time
            logger.debug("Button State:"+str(button_state))
            logger.debug("Iteration:"+str(i))
            print(button_state)
            print(i)
            if button_state == 0:
                if i % 60 == 0:
                    print("Button released")
                    logger.debug("Button Released")
                    with open('/home/linaro/db/live_sensorData.json', 'r') as file:
                        sensor_data = json.load(file)
                    ser.write(json.dumps(sensor_data["ClouzerAQISensorData"]).encode() + b'\n')
                    print("\nSent sensor data:", sensor_data)
                    logger.debug("Sent sensor data:"+str(sensor_data))
                    i = 1
            else:
                print("Button pressed")
                logger.debug("Button Pressed")
                with open('/home/linaro/db/demo_live_sensorData.json', 'r') as file:
                    sensor_data = json.load(file)
                ser.write(json.dumps(sensor_data["ClouzerAQISensorData"]).encode() + b'\n')
                print("\nSent sensor data:", sensor_data)
                logger.debug("Sent sensor data:"+str(sensor_data))
            time.sleep(1)
            i = i+1
    except Exception as e:
        print("An error occurred:", e)
        time.sleep(60)
