# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration
import random
common_list = []
list1 =[]
i =0
while i < 10:
    list1.append(random.randint(1,101))
    i+=1
print('The random list is:',list1)
i=0
while i < len(list1):
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        common_list.append(list1[i])
    i += 1
print('The common list is: ',common_list)
