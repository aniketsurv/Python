import paho.mqtt.client as mqtt
import threading
import time
from G_param import GlobalParams
from mqtt_receiver2 import mqttreceiver  # Import the mqtt_receiver function
from mqtt_sender2 import mqttsender


# MQTT Broker settings
BROKER = "broker.emqx.io"  # Replace with your broker IP or hostname
PORT = 1883
TOPIC_COMMAND = "device/command"
TOPIC_ACK = "device/ack"

# 3. Main function to send commands and validate results
def send_commands_and_validate():
    
    # Start both MQTT threads
    receiver_thread = threading.Thread(target=mqttreceiver.mqtt_receiver,args=(BROKER,PORT))
    sender_thread = threading.Thread(target=mqttsender.mqtt_sender,args=(BROKER,PORT))
    
    receiver_thread.start()
    time.sleep(1)
    sender_thread.start()
    time.sleep(1)
    
# 4. Main script to start everything
if __name__ == "__main__":
    send_commands_and_validate()
