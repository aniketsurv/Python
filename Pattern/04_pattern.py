'''
      *
     * *
    * * *
   * * * *
  * * * * *
  
  '''

row =6

for i in range(1,row):
    space = " "*(row-i)
    star = " *"*(i)
    print(space+star)