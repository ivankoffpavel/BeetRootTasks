# Find the the same numbers in two lists (without using a tuple or set)
list1 = [1,2,3,4,9]
list2 = [1,9]
sum_list = []
for i in list1:
    if i in list2:
        sum_list.append(i)
print(sum_list)