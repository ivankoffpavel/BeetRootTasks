# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
# as attributes. Make another method called talk() which makes prints a greeting from the person containing, for example
#     like this: “Hello, my name is Carl Johnson and I’m 26 years old”.



class Person:
    def __init__(self,name,surname,age):
        self.age = age
        self.surname = surname
        self.name = name
    def talk(self):
        print('Hello,my name is',self.name, self.surname,'and I\'m',self.age,'years old')


person_1 = Person('Vladimir','Zelenskiy',43)
person_1.talk()