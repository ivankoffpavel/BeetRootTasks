# Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
class Dog:
    def __init__(self,dogsage,age_factor=7):
        self.age_factor = age_factor
        self.dogsage = dogsage
    def human_age(self):
        hum_age = self.dogsage*self.age_factor
        print('The human equal age is:',hum_age)
dog1 = Dog(10)
dog1.human_age()
dog2= Dog(5)
dog2.human_age()
