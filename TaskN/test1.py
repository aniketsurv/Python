import time
import paho.mqtt.client as mqtt
from G_param import GlobalParams

# MQTT Broker settings
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_COMMAND = "device/command"
TOPIC_ACK = "device/ack"

# Initialize the MQTT client for sending commands
mqtt_client = mqtt.Client("CommandSender")
mqtt_client.connect(BROKER, PORT, 60)

# Store received ACKs
received_acks = []

# Callback function for receiving ACKs
def on_ack_received(client, userdata, msg):
    ack_message = msg.payload.decode()
    print(f"Received ACK: {ack_message}")
    received_acks.append(ack_message)

# Set the callback for ACK messages
mqtt_client.on_message = on_ack_received
mqtt_client.subscribe(TOPIC_ACK)

commands_to_send = ["ON", "LOW", "MED", "HIGH", "OFF"]

# Simulate sending commands
for command in commands_to_send:
    print(f"Sending command: {command}")
    
    # Set the command in the global parameter storage
    GlobalParams.set_command(command)
    
    # Publish the command to the MQTT broker
    mqtt_client.publish(TOPIC_COMMAND, command)
    
    # Start listening for the acknowledgment
    mqtt_client.loop_start()  # Start loop to listen for ACKs
    
    # Wait for acknowledgment (simulating processing delay)
    time.sleep(2)  # Wait enough time for the receiver to process and send ACK
    
    mqtt_client.loop_stop()  # Stop loop after acknowledgment is handled

# Disconnect the client after sending all commands
mqtt_client.disconnect()
