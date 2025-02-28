import serial
import time

# Open serial port
ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)
ser.flush()
LedFlag = "OFF"

def send_data(data):
    if data is not None:
        try:
            ser.write((data + '\n').encode('utf-8'))
            print(f"Sent: {data}")
        except serial.SerialException as e:
            print(f"Error writing to serial port: {e}")

def receive_data():
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            if data:
                return data
    except serial.SerialException as e:
        print(f"Error reading from serial port: {e}")
    return None
try:
    while True:
        # Example: Send data to ESP32
        if LedFlag == "OFF":
            LedFlag = "ON"
        else:
            LedFlag = "OFF"
        send_data(LedFlag)
        
        # Example: Receive data from ESP32
        received = receive_data()
        if received:
            print("Received:", received)
        
        time.sleep(2)
except KeyboardInterrupt:
    print("Exiting Program")

finally:
    ser.close()
