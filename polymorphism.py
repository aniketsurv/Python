#Polymorphism simply means having many forms.
#polymorphis achived by two ways - method overiding & method overloading

#1) method overriding
#in this example dog & cat class sound method override on Animal class sound 

class Animal:
    print('Animal is mainclass..')

    def sound(self):
        print('Animal sounds')

class dog(Animal):
    print('dog is subclass..')

    def sound(self):
        print('dog barks')


class cat(Animal):
    print('cat is subclass..')

    def sound(self):
        print('cat meows')

dog = dog()
cat = cat()

dog.sound()
cat.sound()

#2) method overloading

