class Student():
    def __init__(self,name,surname,ZNO_test,certificate):
        self.certificate = certificate
        self.name = name
        self.ZNO_test = ZNO_test
        self.surname = surname
    def calc_rating(self):
        if self.certificate == False:
            graduate = 0
        else:
            graduate = 10
        res_rating = self.ZNO_test + graduate
        return res_rating


student_1 = Student('Ivan','Ivankov',25,True)
student_2 = Student('Petro','Mikoluk',15,False)
print(f'The rating of {student_1.name}', student_1.calc_rating())
print(f'The rating of {student_2.name}', student_2.calc_rating())




