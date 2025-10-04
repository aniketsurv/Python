
class square_natural:

    num = int(input("Enter a number : "))

    total = 0
    for i in range(1,num+1):
        total += i**2

    print("sum square of natural number : ", total)


