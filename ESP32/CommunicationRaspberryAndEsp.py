import serial
import time

try:
    # Open serial port (replace '/dev/ttyS0' with the actual serial port)
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    print("Serial port opened successfully.")
    
    while True:
        # Send data to ESP32
        ser.write(b'Hello aniket from Raspberry Pi!\n')
        print("Data sent: Hello from Raspberry Pi...............................!")
        
        # Read data from ESP32
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print(f"Received from ESP32: {response}")
            
        time.sleep(10)  # Wait for 1 second

except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("Exiting program...")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")