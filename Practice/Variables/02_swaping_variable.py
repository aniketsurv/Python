#swapping two numbers using third variable

a = 10
b = 20

c = a
a = b
b = c

print(a)
print(b)

#swapping two numbers without using third variable


x = 20
y = -50

# first way
# x = x+y
# y = x-y
# x= x-y

# second way
x = y-x
y = y-x
x = x+y

print(x)
print(y)


