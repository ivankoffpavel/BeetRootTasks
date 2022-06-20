# Task 2 Mathematician Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
# square_nums(takes a list of integers and returns the list of squares) remove_positives(takes a list of integers and returns
# it without positive numbers filter_leaps(takes a list of dates(integers) and removes those that are not 'leap years'
# ```
# class Mathematician:
#     pass
#
# m = Mathematician()
#
# assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
#
# assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
#
# assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
#
# ```
list1 = [1,-2,7,3,-5]
list2 = [2000,1998,2010,1887]
class InputdData:
    def __init__(self,simple_list,list_of_years):
        self.list_of_years = list_of_years
        self.simple_list = simple_list
    def print_info(self):
        print(f'This class accepts list of numbers {self.simple_list} and list of years{self.list_of_years}')
x = InputdData(list1,list2)
x.print_info()
class Mathematician(InputdData):
    new_list1 =[]
    new_list2 = []
    new_list3 = []
    def square_nums(self):
        for i in self.simple_list:
            Mathematician.new_list1.append(i**2)
        print(Mathematician.new_list1)
    def remove_positives(self):
        for i in self.simple_list:
            if i < 0:
                Mathematician.new_list2.append(i)
        print(Mathematician.new_list2)
    def filter_leaps(self):
        Mathematician.new_list3.append([i for i in self.list_of_years if i%4 == 0])
        print(Mathematician.new_list3)

y = Mathematician(list1,list2)
y.square_nums()
y.remove_positives()
y.filter_leaps()


