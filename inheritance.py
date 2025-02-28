# child class inherit the porperties of parent class is known as inheritance.
# Types -
# 1) single
# 2) multiple
# 3) multilevel
# 4) Heirarchical

#  Example of single inheritance & multilevel
class Animal :
    def parentsound(self): 
        print('Animal sounds')

class cat(Animal):
    def catsound(self):
         print('meow') 
        

class manimeow(cat):
    def sound(self): 
         print('meeeeeow')

c = cat()
manimeow = manimeow()

manimeow.parentsound()
manimeow.catsound()
manimeow.sound()
print("------------------------")


#  Example multiple inheritance
class father:
    def fathersays(self):
        print('fathersays')

class mother:
    def mothersays(self):
        print('mothersays')

class child(father, mother):
    def childsay(self):
        print('childsay')

child = child()
child.fathersays()
child.mothersays()
child.childsay()
print("------------------------")
