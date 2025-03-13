# Abstraction is used to hide internal details and show only functionalities.

from abc import ABC, abstractmethod

class abst(ABC):
    print('abstraction')

    @abstractmethod
    def area(self):
        pass

class Mgst(abst):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

mg = Mgst(10,50)
mg.area()



