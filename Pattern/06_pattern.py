'''
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
'''

row = 5

for i in range(1,row+1):
    space = " "*(row-i)
    star = " *"*i
    print(space+star)


for i in range(1,row):
    space = " "*(i)
    star = " *"*(row-i)
    print(space+star)