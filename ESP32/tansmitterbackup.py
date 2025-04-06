import logging
import serial
import json
import time

logging.basicConfig(level=logging.INFO, filename='sender.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Sender")

ser = serial.Serial('/dev/serial0', 9600, timeout=1)
dummy_data = {'ClouzerAQISensorData': {'SensorID': 47128726470656, 'sensors': [{'comp': 'CO2', 'value': 1018}, {'comp': 'pm10', 'value': 7}, {'comp': 'pm25', 'value': 21}, {'comp': 'temp', 'value': 81}, {'comp': 'hum', 'value': 38}, {'comp': 'voc', 'value': 197}], 'CLG_Speed_Data': [{'comp': 'SPEED', 'value': 'Off'}]}}

reset_data = {'ClouzerAQISensorData': {'SensorID': 91173616091136, 'sensors': [{'REQUEST': 'RESET'}]}}

while True:
    try:
        with open('/home/linaro/db/live_sensorData.json', 'r') as file:
            sensor_data = json.load(file)
        print("\nSent sensor data:", sensor_data)
        ser.write(json.dumps(sensor_data["ClouzerAQISensorData"]).encode() + b'\n')
        time.sleep(1)
        logger.info("Data Sent: %s", sensor_data)  
        acknowledgment = ser.readline().decode().strip()
        print("\nAcknowledgment received:", acknowledgment)
        logger.info("Acknowledgment: %s", acknowledgment)
        
        if acknowledgment:
            try:
                ack_data = json.loads(acknowledgment)
                if ack_data.get("SensorID") == 91173616091136 and ack_data["sensors"][0].get("REQUEST") == "RESET":
                    print("Reset request received, sending reset data.")
                    ser.write(json.dumps(reset_data["ClouzerAQISensorData"]).encode() + b'\n')
                    logger.info("Reset Data Sent: %s", reset_data)
            except json.JSONDecodeError:
                print("Received acknowledgment is not valid JSON")

        time.sleep(60)
    except Exception as e:
        print("An error occurred:", e)
        logger.info("Error Occurred: %s", e)
        ser.write(json.dumps(dummy_data["ClouzerAQISensorData"]).encode() + b'\n')
        time.sleep(60)