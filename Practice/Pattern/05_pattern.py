'''
    *
   **
  ***
 ****    i j
*****    4 0      
 ****    5 1
  ***    6 2
   **
    *
'''

row = 7

# for i in range(1,row+1):
#     space = " "*(row-i)
#     star = "*"*i
#     print(space+star)


# for i in range(1,row):
#     space = " "*(i)
#     star = "*"*(row-i)
#     print(space+star)

# fl=row/2
# print(fl)
# print(type(fl))

for i in range(row):
    for j in range(int(row)):
        if j >row/2 :
            print(" ",end="")
        elif (j+i)+1<=(row/2):
            print(" ",end="")
        elif i>=(row/2) and i-j-1>=row/2-1:
            print(" ",end="")
        else:
            print("*",end="")
        
    print("")