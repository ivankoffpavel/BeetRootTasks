# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their own implementation
# of the method talk be different.For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’. Also, create a simple
# generic function, which takes as input instance of a Cat or Dog classes and performs talk methodon input parameter.
class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Must be implemented by a subclass')
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def talk(self):
        print(f'{self.name} says Meu')
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def talk(self):
        print(f'{self.name} says Woof Woof')
cat1 = Cat('Marusya')
cat1.talk()
dog1 = Dog('Jacke')
dog1.talk()
def type(name):
    return name
type(dog1.talk())
type(cat1.talk())