# 3. Write a program by creating a Person and Employee classes having the following methods and print the final salary.
# 1 - getInfo() in Person class which prints the info of Person
# 2 - getEmpInfo() - takes the salary, number of hours of work per day of employee as parameter
# 3 - 'AddSal()'   which   adds   $10   to   salary   of   the   employee   if   it   is   less   than   $500.
# 3 - 'AddWork()' which adds $5 to salary of employee if the number of hours of work per day is more than 6 hours (отредактировано)
class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def get_info(self):
        print("Name:",self.name,'Surname:',self.surname,self.age)

pers1= Person('Ivan','Ivanov',35)
pers1.get_info()
# class employee:
#     def __init__(self,salary,hours):