a = 10
b = 5
print(f'before swap :')
print(f'a : {a}')
print(f"b : {b}")

a, b = b, a

print(f'after swap :')
print(f'a : {a}')
print(f"b : {b}")


c = 20
d = 30
print(f'before swap :')
print(c)
print(d)
print(f'after swap :')

c = c+d
d = c-d
c = c-d
print(c)
print(d)


