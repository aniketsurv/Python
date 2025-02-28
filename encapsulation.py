# It is used for restrict variable & methods.
# In encapsulation, code & data are rapped together within a single unit 
# Using private attribute & protected attribute achive encapsulation
# 

class car:

    def __init__(self,brand,model):
        self.__brand = brand   #private attribute accicable only with in class
        self._model = model    #protected attribute accible within & derived class

    def get_brand(self):
        return self.__brand

    def set_model(self,model):
        self._model = model

c = car("BMW","star")
print(c.get_brand())

print(c._model)
c.set_model("torado")
print(c._model)


