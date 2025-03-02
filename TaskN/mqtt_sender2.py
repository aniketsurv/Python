import paho.mqtt.client as mqtt
import time
from G_param import GlobalParams
from mqtt_receiver2 import mqttreceiver

TOPIC_ACK = "device/ack"

class mqttsender:
    
    @staticmethod
    def mqtt_sender(BROKER, PORT):
        print("In mqtt_sender")

        while True:
            current_command = GlobalParams.action_command
            action_status = GlobalParams.action_status
            client = mqttreceiver.get_client()
            if action_status:
                # Send back an ACK and set command result to True for successful command
                client.publish(TOPIC_ACK, f"{current_command}")
                print(f"Command processed: {current_command}")    
                GlobalParams.action_status = False
                GlobalParams.action_command = []

            time.sleep(1)
