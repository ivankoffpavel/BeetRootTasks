#Words combination
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)
import random
string=input("Input a string ")
print(''.join(random.sample(string,len(string))))
print(''.join(random.sample(string,len(string))))
print(''.join(random.sample(string,len(string))))
print(''.join(random.sample(string,len(string))))
print(''.join(random.sample(string,len(string))))
x=range(1,10)
print(x)