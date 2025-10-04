'''you simply add up each individual digit of that number. 
   For example:
   For the number 123, the sum of digits is:  1+2+3=6
'''

num = 54321
total = 0

for i in range(len(str(num))):
    print("index : ",i)
    total += int(str(num)[i])

print(f"Sum of digits : {total}")