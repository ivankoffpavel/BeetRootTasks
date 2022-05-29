# Create your own defined exception with custom message (if can be devision by 0 or value error).
# Try to use nested try catch blocks.
a = input('Input the number not equals to 0 or a letter : ')#1 way
try:
    100/int(a)
except ZeroDivisionError:
    print('You symbol is 0,try again!!!')
except ValueError:
    print('You type a letter,try again!!!')

a = input('Input the number not equals to 0 or a letter : ')#2 way
try:
    100/int(a)
except:
    print('Unexcepted error!!!')