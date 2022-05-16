#Write a Python program to check whether a letter is a vowel or consonant.
input_string=input('Input a string with a few characters ')
i=0
vow_count=0
while i < len(input_string):
    if input_string[i] =='a':
        print('The vowel is',input_string[i])
        i+=1
    elif input_string[i] =='e':
        print('The vowel is', input_string[i])
        i += 1
    elif input_string[i] == 'y':
        print('The vowel is', input_string[i])
        i += 1
    elif input_string[i] == 'i':
        print('The vowel is', input_string[i])
        i += 1
    elif input_string[i] == 'o':
        print('The vowel is', input_string[i])
        i += 1
    elif input_string[i] == 'u':
        print('The vowel is', input_string[i])
        i += 1
    else:
        print('The consonent is',input_string[i])
        i += 1

