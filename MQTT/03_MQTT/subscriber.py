import paho.mqtt.client as mqtt

broker = "0.0.0.0"
port = 8886
username = "CEDPython"
password = "@$0uL|?yT#0n"
client_id = "test_local"
subscirbe_topic = "hubAction/controller"
QOS = 0

# Callback when client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to broker")
        client.subscribe((subscirbe_topic,QOS))  # Subscribe to all topics
        print("📡 Subscribed to all topics (#)")
    else:
        print(f"❌ Connection failed with code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"📥 Topic: {msg.topic}")
    print(f"📦 Payload: {msg.payload.decode()}")

# Create and configure the client
client_local = mqtt.Client(client_id)
client_local.username_pw_set(username=username, password=password)
client_local.on_connect = on_connect
client_local.on_message = on_message

# Connect and start loop
client_local.connect(broker, port, keepalive=60)
client_local.loop_forever()
