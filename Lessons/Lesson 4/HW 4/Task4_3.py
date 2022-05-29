# Task 3
# The name check.Write a program that has a variable with your name stored (in lowercase) and then asks for your name as/
# input. The program should check if your input is equal to the stored name even if the given name has another case, e.g./
# , if your input is “Anton” and the stored name is “anton”, it should return True.
my_name = 'pavel'
input_name=input('Input you name ')
if input_name.isalpha() is True:
    if input_name.lower() == my_name:
        print('You evaluation is correct! Welcome!')
    else:
        print('The name is incorrect, try again ')
else:
    print('Name must contain only letters ')