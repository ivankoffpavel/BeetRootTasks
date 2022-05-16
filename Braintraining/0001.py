#write a program wich replaces the special symbols from inputed string
while True:
    user_string=input('Input a string ')
    i=0
    while i < len(user_string):
        if user_string[i].isalpha() or user_string[i].isdigit() is True:
            i+=1
        else:
            new_string=user_string.replace(user_string[i],'')
            i+=1
    print(new_string)