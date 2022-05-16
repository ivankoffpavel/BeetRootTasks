# Finding the average of 5 numbers using while loop
numbers=[1,2,3,4,6]
sum=0
i=0
while i < 5:
    sum+=numbers[i]
    i+=1
print("Average is ",sum/5)