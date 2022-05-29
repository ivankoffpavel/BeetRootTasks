# Create a function where you can generate fandom number and if it’s odd - raise an exception,
# use finally block to print a number.
import random
def number():
    num = random.randint(1,10)
    try:
        if num % 2 != 0:
            raise Exception('The number is odd')
    finally:
        print('The number is:',num)

number()
