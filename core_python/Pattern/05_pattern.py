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