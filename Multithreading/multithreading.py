import threading
import time

def task1():
    for _ in range(5):
        print("Task 1 executing")
        time.sleep(3)

def task2():
    for _ in range(5):
        print("Task 2 executing")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Both threads finished executing")