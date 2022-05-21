# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing/
# the common integers between the 2 initial lists without any duplicates.Constraints: use only while loop and random
# module to generate numbers
import random
list_one=[]
list_two=[]
common_list=[]
#creating a random list 1
i=0
while i < 10:
    list_one.append(random.randint(0,10))
    i+=1
print('Random list one is:',list_one)
#creating a random list 2
i=0
while i < 10:
    list_two.append(random.randint(0,10))
    i+=1
print('Random list two is:',list_two)
i=0
while i < 10:
    if list_one[i] in list_two:
        if list_one[i] not in common_list:
            common_list.append(list_one[i])
    i+=1
print('The common list with exclusive numbers: ', common_list)


