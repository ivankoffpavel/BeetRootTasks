# The valid phone number program. Make a program that checks if a string is in the right format /
# for a phone number.The program should check that the string contains only numerical characters and is only 10 characters long.Print a suitable message depending on the outcome of the string evaluation.
phone_string=input('Input a phone number you want to call ')
if len(phone_string)==10:
    if phone_string.isdigit() is True:
        print(f'The number is correct, {phone_string},\nWould you like to connect?')
    else:
        print('Inputed number is incorrect and contains letters or symbols,try again ')
else:
    print('The number of digits mast be 10, try again ')