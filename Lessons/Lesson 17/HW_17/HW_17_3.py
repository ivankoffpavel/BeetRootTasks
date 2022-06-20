# Task 3
# Fraction Create a Fraction class, which will represent all basic arithmetic logic for fractions (+, -, /, *) with appropriate
# checking and error handling
# ```

class Fraction:
    def __init__(self,num):
        self.num = num
    def print(self):
        print(self.num)

x = Fraction(1/5)
y = Fraction(3/5)
y.print()
print(x+y)

# x = Fraction(1/2)
#
# y = Fraction(1/4)
#
# x + y == Fraction(3/4)
#
# ```