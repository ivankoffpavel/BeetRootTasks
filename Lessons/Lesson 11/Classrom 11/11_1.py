# Write a program that searches the longest word in file
with open('text1.txt','r') as f:
    string = f.read()
    string = string.split()
count = 0
new_list = []
for word in string:
    count =0
    for letter in word:
        count+=1
        new_list.append(count)
print('Max symbols in word',max(new_list))

