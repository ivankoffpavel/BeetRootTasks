#from 10 to 1000 divisible on 7
#1 way
print('1 way')
import random
for i in range(1,6):
    a=random.randint(2,142)
    print(a*7)
#2 way
print('2 way')
import random
c=0
while c<5:
    a=random.randint(10,1000)
    if a%7==0:
        c+=1
        print(a)
