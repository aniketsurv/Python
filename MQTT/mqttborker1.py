import paho.mqtt.client as mqtt
import time

broker = "broker.emqx.io" # Update with your Raspberry Pi's IP address or hostname if needed
port = 1883
client_id = "RaspberryPiClient"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client(client_id)
client.on_connect = on_connect

try:
    client.connect(broker, port, 60)
except ConnectionRefusedError as e:
    print(f"Connection refused: {e}")
    exit(1)
except Exception as e:
    print(f"Error connecting to MQTT broker: {str(e)}")
    exit(1)

client.loop_start()

try:
    while True:
        client.publish("test/topic", "Hello, ESP32!")
        time.sleep(5)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
