import timeit
# Функція Filter дає можливість фільтрувати ітерований обєкт.
x = [1,2,6,45,8,23,90,33,25,7,0,8,21,7,-1]
# res = []
# for i in x:
#     if i > 2:
#         res.append(i)
# print(res)
# #через list comprehension
res = [y for y in x if y > 2]
print(res)
# # filter(function or None,iterable)---------> filter object
multiple = lambda a,b:a*b
print(multiple(2,4))
print(type(filter(lambda it:it > 2,x)))
print(list(filter(lambda it:it > 2,x)))
print(list(filter(None,x)))


