# Write a function that accepts string and try to parse it into integer - use try except to handle exceptions.
x = input('Input number, any letters please: ')
try:
    x = int(x)
except ValueError:
    print('Use any letters, please!!!')
finally:
    print('The symbol is',x)