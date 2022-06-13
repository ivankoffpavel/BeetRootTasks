# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def ext_func(x):
    def in_func(y):
        return x+y
    return in_func
res = ext_func(5) # res is here a function equal to in_func
res1= res(10) # here function res = in_func accepts a parametr y which equals to 10



