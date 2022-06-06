# Write a Python program that read file and to removes newline characters
with open('text1.txt', 'r') as a:
    string = a.readlines()
    print(string)
new_list = []
for i in string:
    new_list.append(i.strip('\n'))
print(new_list)





