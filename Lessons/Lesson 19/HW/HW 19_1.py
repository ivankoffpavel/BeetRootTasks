# Task
# 1
# Create your own implementation of a built - in function enumerate, named`with_index`, which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function
list1 = [1,23,34,5,45,67,3,45]
def with_index(iterable,start=1):
    it = iter(iterable)
    start = 1
    for i in range(len(iterable)):
        print(f'{start}:{next(it)}')
        start += 1


with_index(list1)

