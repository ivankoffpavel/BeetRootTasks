# Write a Python program to check whether a given key already exists in a dictionary
x = int(input('Input a key of dictionary: '))
dic_1 = dict([(2,5),(3,7)])
if x in dic_1:
    print('This key exists in dict')
else:
    print('This key doesn\'t exists in dict')

print(dic_1)