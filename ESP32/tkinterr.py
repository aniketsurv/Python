import tkinter as tk
import random
import time

# Sensor value ranges
LEVELS = [
    ("Low", "#4CAF50"),      # Green
    ("Medium", "#FFC107"),   # Amber
    ("High", "#F44336")      # Red
]

# Create the main window
root = tk.Tk()
root.title("Air Purifier with Sensor Display")
root.geometry("600x250")
root.resizable(False, False)

# ---------------- Purifier Frame ----------------
purifier_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
purifier_frame.pack(side="left", fill="both", expand=True)

title1 = tk.Label(purifier_frame, text="Purifier Status", font=("Arial", 16, "bold"))
title1.pack(pady=10)

purifier_status = tk.Label(purifier_frame, text="Purifier is OFF", font=("Arial", 14))
purifier_status.pack(pady=10)

def toggle_purifier():
    if purifier_status.cget("text") == "Purifier is OFF":
        purifier_status.config(text="Purifier is ON", fg="green")
    else:
        purifier_status.config(text="Purifier is OFF", fg="red")

btn_toggle = tk.Button(purifier_frame, text="Toggle Purifier", command=toggle_purifier)
btn_toggle.pack(pady=10)

# ---------------- Sensor Frame ----------------
sensor_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
sensor_frame.pack(side="right", fill="both", expand=True)

title2 = tk.Label(sensor_frame, text="Sensor Values", font=("Arial", 16, "bold"))
title2.pack(pady=10)

sensor_label = tk.Label(sensor_frame, text="", font=("Arial", 20, "bold"), width=20, height=2)
sensor_label.pack(pady=20)

time_label = tk.Label(sensor_frame, text="", font=("Arial", 10))
time_label.pack()

# Function to update sensor value
def update_sensor():
    level, color = random.choice(LEVELS)
    sensor_label.config(text=level, bg=color, fg="white")
    time_label.config(text=f"Last Updated: {time.strftime('%H:%M:%S')}")
    root.after(2000, update_sensor)  # update every 2 seconds

# Start updating
update_sensor()

# Run the app
root.mainloop()
