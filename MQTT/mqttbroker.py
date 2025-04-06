import paho.mqtt.client as mqtt
import time

broker_address = "broker.emqx.io"

client = mqtt.Client("RPi_LED_Control")
client.connect(broker_address)

# Publish messages to control the LED on ESP32
client.publish("led_control", "1")  # Turn LED ON
time.sleep(1)
client.publish("led_control", "0")  # Turn LED OFF

client.disconnect()
