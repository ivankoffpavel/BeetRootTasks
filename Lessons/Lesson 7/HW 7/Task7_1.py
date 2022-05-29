# Make a program that has some sentence (a string) on input and returns
# a dict containing all unique words as keys and the number of occurrences as values.
str1 = input('Input a sentence: ')
words = str1.split()
dict = {}
for i in words:
    dict[i] = str1.count(i)
print(dict)