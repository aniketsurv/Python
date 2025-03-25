import paho.mqtt.client as mqtt
import time

class Sub:

    __client = None

    topic = 'test/validate'

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result: {rc}")
        # Subscribe to the topic once connected
        client.subscribe(Sub.topic)

    @staticmethod
    def on_disconnect(client, userdata, rc):
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

        Sub.__client = mqtt.Client("SubscriberClient")  # Specify MQTTv3.1.1 protocol
        
        Sub.__client.enable_logger() # Enable logging for track mqtt issue 

        # Bind event handlers
        Sub.__client.on_connect = Sub.on_connect
        Sub.__client.on_disconnect = Sub.on_disconnect
        Sub.__client.on_message = Sub.on_message

        # Connect to the broker
        Sub.__client.connect(broker, port, 60)

        Sub.__client.loop_forever()
        # Start the MQTT loop to handle messages
        # client.loop_start()
        # time.sleep(50)
        # client.loop_stop()

# Start the MQTT subscriber
Sub.mqtt_connection()
