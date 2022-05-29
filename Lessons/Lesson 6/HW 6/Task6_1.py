# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random
list = []
i=0
while i < 11:
    list.append(random.randint(0,10))
    i+=1
print(list)
print(f'The max value of list is:{max(list)}')