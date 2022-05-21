# The math quiz program
# Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,/
# and then responds with a message accordingly.
print('Count a result of equation  "4*2-3/1**3" ')
res = 4 * 2 - 3 / 1 ** 3
res1 = input('Input an answer ')
if res1.isalpha():
    print("The answer must be a number!!!!")
else:

    if float(res1) == res:
        print("Your answer is correct!!!")
    else:
        print("Your answer is incorrect!!!")
