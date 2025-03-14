class natural_number:
    
    number = int(input("Enter natural number : "))

    total =0

    for n in range(1,number+1):
        total += n
    
    print(f"sum of {number} natural number are : ",total)
