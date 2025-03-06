import paho.mqtt.client as mqtt
from G_param import GlobalParams

TOPIC_COMMAND = "device/command"

class mqttreceiver:
    __client = None
    
    @classmethod
    def get_client(cls):
        return mqttreceiver.__client
    
    def on_connect(client, userdata, flags, rc):
        print(f"Connected to MQTT broker with result code {rc}")
        client.subscribe(TOPIC_COMMAND)

    def on_message(client, userdata, msg):
        
        command = msg.payload.decode()
        print(f"Received command: {command}")
        
        GlobalParams.action_command.append(command)
        
        print("GlobalParams.action_command-->",GlobalParams.action_command)
        GlobalParams.action_status = True
        
    # MQTT receiver thread
    def mqtt_receiver(BROKER,PORT):
        mqttreceiver.__client = mqtt.Client("Receiver")
        mqttreceiver.__client.on_connect = mqttreceiver.on_connect
        mqttreceiver.__client.on_message = mqttreceiver.on_message

        mqttreceiver.__client.connect(BROKER, PORT)
        mqttreceiver.__client.loop_forever()
