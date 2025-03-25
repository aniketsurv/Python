import paho.mqtt.client as mqtt
import time
class Pub:

    __client = None

    @staticmethod
    def broadcast():
        # Publish a message after successful connection
        print("Publish on topic test/validate")
        Pub.__client.publish("test/validate", "Hello world!")

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print(f"Connected with result: {rc}")
        client.publish("test/validate", "Hello world!")
        
    @staticmethod
    def on_disconnect(client, userdata,rc):
        print(f"Disconnected with result: {rc}")

    @staticmethod
    def mqtt_connection():
        print("In publisher mqtt connection")

        broker = "broker.hivemq.com"
        port = 1883

        Pub.__client = mqtt.Client("PublisherClient")  # Specify MQTTv3.1.1 protocol
        
        Pub.__client.enable_logger()  # Enable logging for track mqtt issue 

        # Bind event handlers
        Pub.__client.on_connect = Pub.on_connect
        Pub.__client.on_disconnect = Pub.on_disconnect

        # Connect to the broker
        Pub.__client.connect(broker, port, 60)


        Pub.__client.loop_forever()
        # Start the MQTT loop to handle messages
        #Pub.__client.loop_start()
        time.sleep(2)
        #Pub.__client.loop_stop()

# Start the MQTT publisher
Pub.mqtt_connection()
time.sleep(2)
#Pub.broadcast()
