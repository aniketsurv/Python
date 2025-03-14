import math

class area_of_circle:
    
    # 1st way
    radius = 4
    arc = 2.14 *radius*radius
    print("area of circle",arc)

    # 2nd way
    rad = int(input("Enter the radius of the circle : "))

    area = math.pi * rad ** 2
    print(f"The area of the circle with radius {rad} is:",area)