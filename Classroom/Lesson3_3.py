#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
# 1 way
i=0
while i < 7:
    if i==3 or i==6:
        i+=1
        continue
    print(i)
    i+=1
#2 way
i=0
while i < 7:
    if i % 3 ==0:
        i+=1
        continue
    print(i)
    i+=1
