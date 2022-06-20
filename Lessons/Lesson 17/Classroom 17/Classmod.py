# Exercise 1
# Create class Car.
# Make all of the variables in the Car class private.
# Try to print one from outside the class.
# Modify the move_forward method to use the private variable model, and call it.
# Create a setter method for one of the variables.
# Use the setter method that you created to change the value of a variable.
# Create a getter method for the same variable as the setter method.
# Use your getter method to access and print out that variable.
class Car:
    def __init__(self,model,brand,type):
        self.__type = type
        self.__brand = brand
        self.__model = model
    def print_car(self):
        print(self.__type)
    def move_forward(self):
        print(f'The model is {self.__model}')
    def get_model(self):
        return self.__model
    def set_model(self,mod_name):
        self.__model = mod_name

Lada = Car('Kalina','Lada','light_car')
Lada.print_car()
Lada.move_forward()
print('The type of car is:',end='')
Lada.print_car()
print('After setter method:',end='')
Lada.print_car()





