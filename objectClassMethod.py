class Animal :
    
    #A class is a collection of objects.

    # Some points on Python class:  
    # Classes are created by keyword class.
    # Attributes are the variables that belong to a class.
    # Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

    temp = 'King'

    def __init__(self):  
        def rrr():
            print('SSS')
        print("Hiii")
        rrr()  
        

temp = Animal()   

class dog :

    #class attribute
    attr1 = "pitbull"

    attr2 = ""
    
    #instance attribute
    def __init__(self, name):
        self.name = name

   
#The object is an runtime entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.
roger = dog('tommy')

# Accessing class attributes
print(f'Dog name is {roger.attr1}')

#Accessing instance attributes
print(f'Dog name is {roger.name}')

#assign value to class attributes
roger.attr2 = 'moti'
print(f'Dog name is {roger.attr2}')