import paho.mqtt.client as mqtt
import time
class Pub:

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result: {rc}")
        # Publish a message after successful connection
        client.publish("test/validate", "Hello world!")

    @staticmethod
    def on_disconnect(client, userdata, flags, rc):
        print(f"Disconnected with result: {rc}")

    @staticmethod
    def mqtt_connection():
        print("In publisher mqtt connection")

        broker = "broker.hivemq.com"
        port = 1883

        client = mqtt.Client("PublisherClient")  # Specify MQTTv3.1.1 protocol
        
        client.enable_logger()  # Enable logging

        # Bind event handlers
        client.on_connect = Pub.on_connect
        client.on_disconnect = Pub.on_disconnect

        # Connect to the broker
        client.connect(broker, port, 60)


        client.loop_forever()
        # Start the MQTT loop to handle messages
        # client.loop_start()
        # time.sleep(2)
        # client.loop_stop()

# Start the MQTT publisher
Pub.mqtt_connection()
