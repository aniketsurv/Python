import tkinter as tk
import random
import time
import threading

# Logic to determine purifier mode
def get_purifier_mode(air_quality):
    if air_quality <= 100:
        return "Low", "green"
    elif 100 < air_quality <= 200:
        return "Medium", "orange"
    else:
        return "High", "red"

# Function to update sensor values
def update_values():
    while running:
        temperature = round(random.uniform(20, 30), 1)
        humidity = round(random.uniform(40, 60), 1)
        air_quality = random.randint(0, 500)

        mode, color = get_purifier_mode(air_quality)

        # Update GUI
        temp_var.set(f"{temperature} °C")
        hum_var.set(f"{humidity} %")
        aqi_var.set(str(air_quality))
        purifier_var.set(mode)
        purifier_label.config(bg=color)

        time.sleep(2)

# Tkinter GUI setup
root = tk.Tk()
root.title("Air Purifier Sensor Dashboard")
root.geometry("300x250")

temp_var = tk.StringVar()
hum_var = tk.StringVar()
aqi_var = tk.StringVar()
purifier_var = tk.StringVar()

tk.Label(root, text="Temperature:", font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=temp_var, font=("Arial", 14)).pack()

tk.Label(root, text="Humidity:", font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=hum_var, font=("Arial", 14)).pack()

tk.Label(root, text="Air Quality Index:", font=("Arial", 12)).pack(pady=5)
tk.Label(root, textvariable=aqi_var, font=("Arial", 14)).pack()

tk.Label(root, text="Purifier Mode:", font=("Arial", 12)).pack(pady=5)
purifier_label = tk.Label(root, textvariable=purifier_var, font=("Arial", 14), width=10)
purifier_label.pack()

running = True
threading.Thread(target=update_values, daemon=True).start()

root.protocol("WM_DELETE_WINDOW", lambda: stop_app())
def stop_app():
    global running
    running = False
    root.destroy()

root.mainloop()
