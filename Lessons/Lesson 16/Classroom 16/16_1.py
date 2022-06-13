# Create2 classes: basic - student; derivative - student with a certificate of achievement)
# Basic class (student):
# Variables: name, age, higher education institution.
# Methods: assignments of higher education institution; name change;
# input-output of age information; output of all data.
# Derivative class: a student with a certificate of achievement - an array of grades is added to the base class.


class Student:
    def __init__(self, name, age):
        self.institution = None
        self.age = age
        self.name = name

    def set_institution(self, institution):
        self.institution = institution

    def __repr__(self):
        return f'name: {self.name}\n' \
               f'age: {self.age}\n' \
               f'high_education_institution: {self.institution}'


class Derivative(Student):
    def __init__(self, name, age, SI, BankAccount):
        super(Derivative, self).__init__(name, age)
        self.BankAccount = BankAccount
        self.SI = SI

    def __repr__(self):
        return f'name: {self.name}\n' \
               f'age: {self.age}\n' \
               f'high_education_institution: {self.institution}\n' \
               f'SI: {self.SI}\n' \
               f'Bank: {str(self.BankAccount)}'

    def name_change(self, name):
        self.name = name

    def bank(self):
        print(self.BankAccount)


student1 = Derivative('Dan', '18', [5, 4, 5, 3], 51687777777)
student1.set_institution('KPI')
print(student1)
student1.name_change('Mark')
print(student1)