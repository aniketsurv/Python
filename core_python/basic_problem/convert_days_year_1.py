class MyClass:
    no_of_days = 380

    def calculate_years_month_weeks_days(no_of_days=None):

        print(f"Number of days :: {no_of_days}")

        year = int(no_of_days/365)
        print(f"Year :: {year}")
        rem1 = int(no_of_days%365)
        print(f"rem1 :: {rem1}")
        Month =int(rem1/30)
        print(f"Month :: {Month}")
        rem2 = rem1%30
        print(f"rem2 :: {rem2}")
        Weeks = int(rem2/7)
        print(f"Weeks :: {Weeks}")
        days = (rem2%7)
        print(f"days :: {days}")

    calculate_years_month_weeks_days(no_of_days=no_of_days)

    

