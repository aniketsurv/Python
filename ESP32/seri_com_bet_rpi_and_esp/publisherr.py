import paho.mqtt.client as mqtt
import time

# MQTT broker connection details
broker_address = "192.168.30.38"   # broker= "0.0.0.0" / "192.168.30.38"
port = 1883                  #  1883 / 8884 /8886

# Create a client instance
client = mqtt.Client("Publisher")

# Connect to broker
client.connect(broker_address, port)

#Publish messages
# for i in range(5):
#     message = f"Message {i+1}"
#     topic = "control/led"
#     client.publish(topic, message)
#     print(f"Published: '{message}' to topic '{topic}'")
#     time.sleep(1)  # Wait for 1 second between messages

ledFlag = False
color = "Red"
while True:
    ledFlag = not ledFlag
   # message = f"Message {ledFlag}"
    message = f"{color}{ledFlag}"
    topic = "control/led"
    client.publish(topic, message)
    print(f"Published: '{message}' to topic '{topic}'")
    time.sleep(3)  # Wait for 3 second between messages

# Disconnect from broker
client.disconnect()
