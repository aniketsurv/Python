'''

*      
**    
***  
****
*****

'''

size = 5

# print("Using one for loop")

# for i in range(1,size):
#     print("*" * i)

# print("Using two for loop")

# for i in range(1,size):
#     for j in range(1,size):
#         if j-i ==0:
#             print("*"*j)


# print("----using while loop----")

for i in range(size):
    for j   in range(size):
        if(j-i<=0):
            print("* ", end="")
    print("")