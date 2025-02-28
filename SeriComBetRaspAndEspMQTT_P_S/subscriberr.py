import paho.mqtt.client as mqtt
import serial

# MQTT broker connection details
broker_address = "0.0.0.0"      # broker= "0.0.0.0" / "192.168.30.38"
port = 8884            #  1883 / 8884 /8886

# Serial port details (adjust as per your ESP32 setup)
serial_port = '/dev/ttyS0'  # Example, adjust based on your actual serial port
baud_rate = 9600  # Example, adjust based on your ESP32 configuration

# Initialize the serial connection
serial_connection = serial.Serial(serial_port, baud_rate, timeout=5)

# Callback function to handle incoming messages
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")
    
    # Send the received MQTT message to ESP32 via serial
    serial_connection.write(message.payload + b'\n')  # Ensure to add newline character if needed
    print(f"Sent message '{message.payload.decode()}' to ESP32 via serial")

# Create a client instance
client = mqtt.Client("Subscriber")

# Assign callback function
client.on_message = on_message

# Connect to broker
client.connect(broker_address, port)

# Subscribe to topic
topic = "control/led"
client.subscribe(topic)
print(f"Subscribed to topic '{topic}'")

# Loop to process incoming messages
client.loop_forever()

# Close serial connection when exiting
serial_connection.close()