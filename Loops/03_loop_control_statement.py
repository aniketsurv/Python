'''
break: Exits the loop prematurely.
continue: Skips the current iteration and moves to the next iteration of the loop.
pass: Does nothing, but it’s a placeholder.

'''


for i in range(10):
    if i == 3:
        break   # Exit the loop when i is 3
    print(i)

print("--------")

for i in range(6):
    if i == 3 :
        continue   # Skip when i is 3
    print(i)

print("--------")

for i in range(6):
    if i == 3 :
        pass
    print(i)
