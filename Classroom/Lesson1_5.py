# the program accepts from user a number and prints back a square root of this number
import math
while True:
    a=(float(input('Input a nubmer ')))
    s=a**0.5#first way
    f=math.sqrt(a)#second way
    print('A square root from this number first way',s)
    print('A square root from this number second way', f)