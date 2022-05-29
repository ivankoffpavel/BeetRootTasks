# Write function that sums up all numbers that are passed to it (*args used)
def sum_num(*args):
    count = 0
    for i in args:
        count+=i
    print("The sum is: ",count)
sum_num(1,2,3,5,6)