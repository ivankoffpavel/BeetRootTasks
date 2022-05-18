# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
i=0
while i <= 5:
    i+=1
    if i % 3 == 0:
        continue
    print(i)