import serial, json

PORT = "/dev/pts/12"
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
print(f"Connected to {PORT} at {BAUD_RATE} baud")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            print(f"Received: {data}")
        except json.JSONDecodeError:
            print(f"Invalid data: {line}")
