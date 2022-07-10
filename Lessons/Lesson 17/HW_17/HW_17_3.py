# Fraction
# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів(+, -, /, * ) з належною перевіркою й обробкою
# помилок.Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction
class Fraction:
    def __init__(self,num,denum):
        self.num = num
        self.denum = denum

    def __add__(self, other):
        if not isinstance(other,type(self)):
            raise ValueError('Not valid operand!')
        if self.denum == other.denum:
            return (self.num + other.num,self.denum)
        elif self.denum != other.denum:
            com_denum = self.denum*other.denum # common denumerator
            return (int((self.num * (com_denum/self.denum)) + (other.num * (com_denum/other.denum))),com_denum)

    def __sub__(self, other):
        if not isinstance(other,type(self)):
            raise ValueError('Not valid operand!')
        if self.denum == other.denum:
            return (self.num - other.num,self.denum)
        elif self.denum != other.denum:
            com_denum = self.denum*other.denum # common denumerator
            return (int((self.num * (com_denum/self.denum)) - (other.num * (com_denum/other.denum))),com_denum)

    def __mul__(self, other):
        if not isinstance(other,type(self)):
            raise ValueError('Not valid operand!')
        return (self.num*other.num,self.denum*other.denum)


    def __truediv__(self, other):
        if not isinstance(other,type(self)):
            raise ValueError('Not valid operand!')
        return(self.num * other.denum,self.denum * other.num)
    def __lt__(self, other):
        com_denum = self.denum * other.denum  # common denumerator
        if (self.num * (com_denum/self.denum)) < (other.num * (com_denum/other.denum)):
            return True
        else:
            return False







x = Fraction(1,4)
y = Fraction(1,2)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x>y)