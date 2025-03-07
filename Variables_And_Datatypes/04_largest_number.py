# Find the Largest of Three Numbers
# Find the Maximum of Three Numbers

#Using if statements

a=30
b=50

if a>b:
    print(a)
else:
    print(b)

#using max()
first= input("first number : ")
second= input("second number : ")

max_number = max(first,second)
print(max_number)

#using sorting

first= input("first number : ")
second= input("second number : ")

numbers = [first,second]
sor = sorted(numbers)
print(sor[-1])



