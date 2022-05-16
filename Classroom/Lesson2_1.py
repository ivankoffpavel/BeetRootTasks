#Find a last position of given substring Emma
s='Emma likes apples, Emma is beautiful'
print(s.rfind('Emma'))
#Return a given substring from a string
s1='The weather is beautiful. But is too hot'
b='hot'
print(s1.count(b))
# # Exercise: Insert the correct syntax to add a placeholder for the age parameter
# age='33'
age='33'
print(f'My age is {age}')
print('My age is {}'.format(age))
print('My age is %s' %(age))
# Exercise: Return the string without any whitespace at the beginning or the end
# s=input("Input a string")
# 1 way
# string=input("Input a string ")
# print(string.strip())
# 2 way
string=input("Input a string \t")
if string[0]==' ':
    string=string[1:len(string)]
if string[len(string)-1]==' ':
    string=string[0:len(string)-1]
print(f'"{string}"')
#3 way
string='  Hi dear Friend '
for i in string:
    while sring[i]==' ':
        string=string.replace(' ','')
print(string)





