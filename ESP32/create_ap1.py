import subprocess
import time

# Function to start the access point
def start_access_point():
    print("Starting access point...")

    # Start hostapd
    subprocess.call(["sudo", "systemctl", "start", "hostapd"])

    # Start dnsmasq
    subprocess.call(["sudo", "systemctl", "start", "dnsmasq"])
    
    print("Access point started successfully.")
    

# Function to stop the access point
def stop_access_point():
    print("Stopping access point...")

    # Stop hostapd
    subprocess.call(["sudo", "systemctl", "stop", "hostapd"])

    # Stop dnsmasq
    subprocess.call(["sudo", "systemctl", "stop", "dnsmasq"])

    print("Access point stopped.")

# Main function
if __name__ == "__main__":
    try:
        start_access_point()
        # Keep the access point running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_access_point()