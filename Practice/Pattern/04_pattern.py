'''
      *
     * *
    * * *
   * * * *
  * * * * *
  
  '''

row =5

# for i in range(1,row):
#     space = " "*(row-i)
#     star = " *"*(i)
#     print(space+star)

for i in range(row):
    for j in range(row):
        if j+i>=row- 1:
            print("* ",end="")
        else:
            print(" ",end="")
    print("")