'''
    *
   **
  ***
 ****
*****

'''

# i j = 
# 0 4

# 1 3

# 2 2
row = 5

# for i in range(1,row+1):
#     space = " "*(row-i)
#     star = "*"*i
#     print(space+star)


for i in  range(row):
    for j in range(row):
        if (j+i)>=row-1:
            print((i),end="")
        else:
            print(" ",end="")
    print("")