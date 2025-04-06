import paho.mqtt.client as mqtt
import time

# MQTT settings
broker = "broker.emqx.io"  # If the broker is running on the same machine broker = "0.0.0.0"  
topic = "test/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

try:
    while True:
        client.loop_start()
        client.publish(topic, "Hello from Raspberry Pi")
        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting Program")
finally:
    client.loop_stop()
    client.disconnect()
