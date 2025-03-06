import time
import paho.mqtt.client as mqtt
from G_param import GlobalParams

# MQTT Broker settings
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_COMMAND = "device/command"
TOPIC_ACK = "device/ack"


mqtt_client = mqtt.Client("CommandSender")
mqtt_client.connect(BROKER, PORT)


received_acks = []

def on_ack_received(client, userdata, msg):
    ack_message = msg.payload.decode()
    print(f"Received ACK: {ack_message}")
    received_acks.append(ack_message)


mqtt_client.on_message = on_ack_received
mqtt_client.subscribe(TOPIC_ACK)

commands_to_send = ["ON", "LOW", "MED", "HIGH", "OFF"]


for command in commands_to_send:
    print(f"Sending command: {command}")
    mqtt_client.publish(TOPIC_COMMAND, command)
    mqtt_client.loop_start()  
    time.sleep(2)  
    mqtt_client.loop_stop() 

# Disconnect the client after sending all commands
mqtt_client.disconnect()
