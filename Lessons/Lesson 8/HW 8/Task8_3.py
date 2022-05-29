# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the
# second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42
def make_operation(*args):
    if args[0] == '+':
        sum1 = 0
        for i in range(1,len(args)):
            sum1 += args[i]
    elif args[0] == '-':
        sum1 = 0
        for i in range(1,len(args)):
            sum1 -= args[i]
    else:
        sum1 = 1
        for i in range(1,len(args)):
            sum1 *= args[i]

    print(sum1)
make_operation('*',1,2,3)