# Try to execute a function that returns a some number, raise an exception when 0 or 100 is returned.
import random
def ran_num():
    list =[0,100,10,2,3,4]
    x = random.choice(list)
    if x ==0 or x == 100:
        raise Exception("Number is 0 or 100!!!")
    print(x)
ran_num()