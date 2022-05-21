# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random
rand_num = str(random.randint(1000000000,9999999999))
print(f'The generated number is: {rand_num}')
new_list=[]
i=0
while i < len(rand_num):
    new_list.append(rand_num[i])
    i+=1
print('The max digit of generated number is: ',max(new_list))