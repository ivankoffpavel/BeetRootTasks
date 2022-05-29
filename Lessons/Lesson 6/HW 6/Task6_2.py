# Task 2
# Exclusive common numbers. Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third
# list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random
i = 0
list1 = []
list2 = []
common_list = []
while i < 11:
    list1.append(random.randint(1,10))
    i +=1
print('The first list: ',list1)
i=0
while i < 11:
    list2.append(random.randint(1,10))
    i +=1
print('The second list: ',list2)
k = 0
while k < len(list1):
    if list1[k] in list2:
        if list1[k] not in common_list:
            common_list.append(list1[k])
    k+=1
print('The common list: ',common_list)


