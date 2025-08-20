# esp32_simulator.py
import time, json

esp_port = "/dev/pts/11"
with open(esp_port, "w") as esp:
    while True:
        payload = {
            "sensor_id": "esp001",
            "temperature": round(20 + 10 * time.time() % 1, 1),
            "humidity": round(40 + 20 * time.time() % 1, 1)
        }
        esp.write(json.dumps(payload) + "\n")
        esp.flush()
        time.sleep(2)
