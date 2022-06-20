# Make a class structure in python representing people at school.Make a base class called Person, a class called Student,
# and another one called Teacher.Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.For example, the name should be a Person attribute, while salary should
# only be available to the teacher.
class Person:
    def __init__(self, firstame, lastname, date_of_birth):
        self.date_of_birth = date_of_birth
        self.lastname = lastname
        self.firstame = firstame
    def print_person_info(self):
        print('Name is:',self.firstame,'Lastname is:',self.lastname,'date of birth is:',self.date_of_birth)
pers_1 = Person('Brianna','Fox',1982)
pers_1.print_person_info()
class Student(Person):
    def __init__(self,firstname,lastname,date_of_birth,specialization,graduade_rate,attendance_rate):
        super().__init__(firstname, lastname, date_of_birth)
        self.attendance_rate = attendance_rate
        self.graduade_rate = graduade_rate
        self.specialization = specialization

    def student_info(self):
        print(f"The student{self.firstame} {self.lastname} of {self.date_of_birth}")
        print(f"Specialization is:{self.specialization} ,graduate rate in percent:{self.graduade_rate}attendance rate in percent:{self.attendance_rate}")
class Teacher(Person):
    def __init__(self,firstname,lastname,date_of_birth,salary):
        super().__init__(firstname,lastname,date_of_birth)
        self.salary = salary

    def teacher_info(self):
        print(f'Name is:{self.firstame},Lastname is:{self.lastname},date of birth is:{self.date_of_birth}salary is:{self.salary}')


Stud1 = Student('Ivan','Marrow',1979,'building construction',75, 90)
Stud1.student_info()
teach1= Teacher('Mike','O\'relly',1984,3000)
teach1.teacher_info()

