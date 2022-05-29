# Create a function that takes on an input random ints (between 1 and 10) and returns the list, without
# duplicates. Try to create two versions of this function - first with usage set and list constructors and
# second only using for-in loops.
# def task2(1,2,34,2,3,2,4) -> 1, 2, 34, 3, 4

def dublicates_func(*args): # 1 way with for loop and list
    res_list =[]
    for i in args:
        if i not in res_list:
            res_list.append(i)

    print(res_list)
dublicates_func(1,2,3,5,5,6,6,6,8,8,10,7)

def dublicate_func1(*args):# 2 with for loop and set
    my_set = set()
    for i in args:
        my_set.add(i)
    print(my_set)
dublicate_func1(1,2,3,5,5,6,6,6,8,8,10,7)
