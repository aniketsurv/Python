import paho.mqtt.client as mqtt
import time

class Sub:

    topic = 'test/validate'

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result: {rc}")
        # Subscribe to the topic once connected
        client.subscribe(Sub.topic)

    @staticmethod
    def on_disconnect(client, userdata, flags, rc):
        print(f"Disconnected with result: {rc}")

    @staticmethod
    def on_message(client, userdata, msg):
        # Print the topic and payload of the received message
        print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

    @staticmethod
    def mqtt_connection():
        print("In subscriber mqtt connection")

        broker = "broker.hivemq.com"
        port = 1883

        client = mqtt.Client("SubscriberClient")  # Specify MQTTv3.1.1 protocol
        
        client.enable_logger()  # Enable logging

        # Bind event handlers
        client.on_connect = Sub.on_connect
        client.on_disconnect = Sub.on_disconnect
        client.on_message = Sub.on_message

        # Connect to the broker
        client.connect(broker, port, 60)

        client.loop_forever()
        # Start the MQTT loop to handle messages
        # client.loop_start()
        # time.sleep(50)
        # client.loop_stop()

# Start the MQTT subscriber
Sub.mqtt_connection()
