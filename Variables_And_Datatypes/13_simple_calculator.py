class calculator:

    def divison(a,b):
        print("",a%b)
    
    def multiplication(a,b):
        print("",a*b)
    
    def substraction(a,b):
        print("",a-b) 
    
    def addition(a,b):
        print("",a+b) 
    
    while True:

        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice(1/2/3/4): ")
        if choice == "1":
            addition(a,b)
        elif choice == "2":
            substraction(a,b)
        elif choice == '3':
            multiplication(a,b)
        elif choice == '4':
            divison(a,b)
        else:
            print("Wrong number")
        
        next_calculation = input("Do you want to continue next calculation? (yes/no) : ")

        if next_calculation == 'no':
            break


        