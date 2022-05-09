#1 way
print('1 way')
a=input("Input sting with letters and digits ")
spisok=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = 0

for i in a:
    if i in spisok:
        letters+=1
print('Letters ',letters)
digit=(len(a)-letters)
print('Digit',digit)
# 2 way
print('2 way')
a=input("Input sting with letters and digits ")
spisok=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters = 0
digit=0

for i in a:
    if i in spisok:
        letters+=1
    else:
        digit+=1
print('Letters ',letters)

print('Digit',digit)
#3 way it seems to me the shortest
print('3 way')
a=input("Input sting with letters and digits ")#input enter a string remember!!!
spisok=['1','2','3','4','5','6','7','8','9','0']
letters=0
digits=0
for i in a:
    if i in spisok:
        digits+=1
    else:
        letters+=1
print(digits,letters)



