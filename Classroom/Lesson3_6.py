#Finding the factorial of number (with while loop)
number=int(input('Input a number '))
i=1
factor=1
while i <= number:
    factor=factor*i
    i += 1
print('Factorial is ',factor)