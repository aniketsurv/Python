import paho.mqtt.client as mqtt
import time
from G_param import GlobalParams
from mqtt_receiver2 import mqttreceiver

TOPIC_ACK = "device/ack"

class mqttsender:

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print(f"Connected to MQTT broker with result code {rc}")
        
    @staticmethod
    def on_message(client, userdata, msg):
        # Just to acknowledge reception of the ACK message
        print(f"Received ACK: {msg.payload.decode()}")

    # MQTT sender thread
    @staticmethod
    def mqtt_sender(BROKER, PORT):
        print("In mqtt_sender")
        client = mqtt.Client("Sender")
        client.on_connect = mqttsender.on_connect
        client.on_message = mqttsender.on_message
        
        client.connect(BROKER, PORT)
        
        # Start the MQTT client loop in the background
        client.loop_start()

        # Loop to periodically check for new commands and test them
        while True:
            current_command = GlobalParams.action_command
            action_status = GlobalParams.action_status
            
            if action_status:
                # Send back an ACK and set command result to True for successful command
                client.publish(TOPIC_ACK, f"{current_command}")
                print(f"Command processed: {current_command}")    
                GlobalParams.action_status = False
                GlobalParams.action_command = []

            time.sleep(1)  # Avoid tight looping, allowing other threads to run
