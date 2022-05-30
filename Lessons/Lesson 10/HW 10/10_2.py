# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns
# the value of squared a divided by b, construct a try-except block which raises an exception if the two values given
# by the input function were not numbers, and if value b was zero (cannot divide by zero).
a = input('Input a first number: ')
b = input('Input a secon number: ')
def numb_correct(a,b):
    try:
        a = int(a)
        b = int(b)
        a/b
    except (ZeroDivisionError,ValueError):
        print('The number is incorrect!!!!')
    else:
        return a**2/b
print('Result is:',numb_correct(a,b))