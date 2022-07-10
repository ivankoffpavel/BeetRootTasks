# class Firstclass:
#     'A class that use two attributes adding'
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def do_somthing(self,temp):
#         # print(f'A:{self.a},B:{self.b}')
#         return self.a + self.b,Firstclass(self.a + self.b,self.a + self.b)
# x = Firstclass(1,2)
# y = Firstclass(3,5)
# print(y)
#
# z = x.do_somthing(y)
#
# h=z[1]
# print(f'a:{h.a},b:{h.b}')
# y = h.do_somthing(h)
# print(z[1].a,z[1].b)
# print(Firstclass.__doc__)
# def f1(self, x, y):
#     return min(x, x+y)
#
# class C:
#     f = f1
#
#     def g(self):
#         return 'hello world'
# x=C
# print(x.f)
# print(object)
# class Foo:
#     'This class is empty'
#     pass
# print(Foo.__doc__)
#
#
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
# x = Employee('Jane',2500)
# x.displayEmployee()
# x.name = 'Ann'
# x.displayEmployee()
# Employee.name = 'call'
# print(x.name)
# print(hasattr(x,'name'))
# print(getattr(x,'salary'))
# setattr(x,'salary',10000)
# print(getattr(x,'salary'))
# #print(Employee.__dict__)
# print(Employee.__module__)
# print(Employee.__bases__)
# def add_x(x):
#     x**2
#     return add_x(2)
# import time
# def decor_func(fun):
#     def wrap(*args,**kwargs):
#        res = fun(*args,**kwargs)*100
#        return res
#     return wrap
#
# @decor_func
# def add(x,y):
#     return (x+y)**2
# print(add(2,1))
#
#
# def time_check(func):
#     def wrapper(*args,**kwargs):
#         start =time.time()
#         res = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__ + ' ' + 'took' + ' ' + str((end-start)*1000) + 'ms')
#         return  res
#     return wrapper
# @time_check
# def sqare_list(lst:list)->list:
#     new_list = []
#     for i in lst:
#         new_list.append(i**2)
#     return new_list
# print(sqare_list([1,2,1,4,5,66,4,4,45,66,77,158,44,55,7,8,9,6,5,21,565]))
l = [1,2,3]
l_it = iter(l)
print(next(l_it))
print(next(l_it))
print(next(l_it))
print(l_it)
str = 'python'
# class Reverse:
#     def __init__(self,data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         else:
#             self.index -=1
#             return self.data[self.index]
#
# for item in Reverse(str):
#     print(item,end='')
def Reverse(data):
    for i in range(len(data)-1,-1,-1):
        yield data[i]
print(Reverse(str))
for item in Reverse(str):
    print(item,end='')
gen_expr = (i**3 for i in range(10) if i % 2 == 0)
print(gen_expr)
for i in gen_expr:
    print(i)
