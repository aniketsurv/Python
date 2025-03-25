'''

*      
**    
***  
****

'''

size = 5

print("Using one for loop")

for i in range(1,size):
    print("*" * i)

print("Using two for loop")

for i in range(1,size):
    for j in range(1,size):
        if j-i ==0:
            print("*"*j)


print("----using while loop----")


j = 1
while j<5:
    print("* " * j)
    print()
    j+=1