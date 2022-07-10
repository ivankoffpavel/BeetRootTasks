# Create a function that accepts list of numbers and return only odd numbers, use typing module.
lst = [1,2,3,5,7,8,9]
def odd_func(a: list[int])->list[int]:
    lst2 =[]
    for i in a:
        if i % 2 != 0:
            lst2.append(i)
    return lst2
print(odd_func(lst))
def odd_func2(a: list[int])->list[int]:
    return [i for i in a if i % 2!= 0 ]
print(odd_func2(lst))




