'''
real life Examples:
1. Loans (Personal, Car, or Home Loans)
2. Fixed Deposits (FDs)

When NOT to Use Simple Interest:
1. Long-Term Investments or Loans

'''

'''
1) If you invest $1000 at an annual interest rate of 5% for 3 years, 
the Simple Interest would be calculated as:

Simple Interest (SI)= P*R*N/100

'''


class simple_interest:
    p = 10000
    r = 20
    n =  2
    
    def calculate_simple_interest(p=None,n=None,r=None):
        print(f"p :: {p}")
        print(f"r :: {r}")
        print(f"n :: {n}")
        
        si = p*n*r/100
        print(f"Calculate SI is : {si}")

    

    calculate_simple_interest(n=n, p=p, r=r)

    

    

    

    