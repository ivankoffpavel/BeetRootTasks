#Write linear and binary search, which one is quicker?
import timeit
list2 = list(range(1,100000))
def common_search(list:int,num:int)->int:
    for i in list:
        if i == num:
            return i
str =  """
list2 = list(range(1,100000))
def common_search(list:int,num:int)->int:
    for i in list:
        if i == num:
            return i
common_search(list2,1987)
            """
print(timeit.timeit(stmt= str, number=1000000))
# print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))



def binary_search(list:int,num:int)->int:
    n = len(list)
    left = 0
    right = n - 1
    while left <= right:
        middle =(left+right)//2
        if num < list[middle]:
            right = middle - 1
        elif num > list[middle]:
            left = middle + 1
        else:
            return middle+1
            raise ValueError
print(binary_search(list2,1987))

