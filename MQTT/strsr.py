import logging
import paho.mqtt.client as paho
import json
import time
from datetime import datetime

# Topics
QOS = 0
driver_topic = [("getProperties_response", QOS)]

class DbMqttConnector:
    __client = ""
    status_res = False

    @classmethod
    def connect_to_db_mqtt(cls, broker, port):
        try:
            # MQTT Client Setup
            DbMqttConnector.__client = paho.Client("newDbconnector")
            DbMqttConnector.__client.on_connect = DbMqttConnector.on_connect
            DbMqttConnector.__client.on_disconnect = DbMqttConnector.on_disconnect
            DbMqttConnector.__client.on_message = DbMqttConnector.on_message

            # Last will message setup in case of unexpected disconnection
            last_will_obj = {"action": "disconnected", "ts": int(datetime.now().timestamp() * 1000), "process": "SoulRouter"}
            DbMqttConnector.__client.will_set("process/status/SoulRouter", json.dumps(last_will_obj), qos=1, retain=False)

            # Set username and password for MQTT connection
            DbMqttConnector.__client.username_pw_set(username="CEDPython", password="@$0uL|?yT#0n")

            # Set max in-flight messages
            DbMqttConnector.__client.max_inflight_messages_set(300)

            # Connect to the broker
            print(f"Connecting to {broker}:{port}...")
            DbMqttConnector.__client.connect(broker, port, 60)

            # Start the MQTT client loop
            DbMqttConnector.__client.loop_forever()  # Change to loop_start() to allow non-blocking loop
        except Exception as e:
            print(f"Error inside connect_to_db_mqtt: {e}")

    @classmethod
    def on_connect(cls, client, userdata, flags, rc):
        try:
            print(f"Connected to MQTT Broker with result code: {rc}")
            # Subscribe to the topics after successful connection
            if rc == 0:
                client.subscribe(driver_topic)
                print("Subscribed to driver topics")
            else:
                print(f"Connection failed with result code {rc}")
        except Exception as e:
            print(f"Error in on_connect: {e}")

    @classmethod
    def on_message(cls, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode('utf-8'))
            print(f"Received message on topic: {msg.topic} with payload: {payload}")
        except Exception as e:
            print(f"Error in on_message: {e}")

    @classmethod
    def on_disconnect(cls, client, userdata, rc):
        print(f"Disconnected from MQTT Broker with result code: {rc}")
        # Attempt to reconnect if disconnected
        if rc != 0:  # Non-zero return code means the disconnect wasn't clean
            print("Reconnecting...")
            client.reconnect()

if __name__ == "__main__":
    # Use the provided broker and port
    broker = "172.17.0.1"  # MQTT Broker IP address
    port = 8886  # MQTT Broker port
    DbMqttConnector.connect_to_db_mqtt(broker, port)
