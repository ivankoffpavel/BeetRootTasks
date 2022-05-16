# Write a python program to find the sum of all even numbers from 0 to 10
i=0
sum=0
while i < 11:
    i+=1
    if i % 2==0:
        sum+=i
        i+=1
print(sum)
