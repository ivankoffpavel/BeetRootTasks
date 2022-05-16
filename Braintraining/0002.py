#For digit from 1 to 100 pass the digits wich are devided on 7
digit_range=range(1,100)
i=0
while i <= len(digit_range):
    i += 1
    if i % 7 == 0:
        continue
    print(i)
#make brake infinity loop function with continue replacing a i+=1
digit_range=range(1,100)
i=1
while i <= len(digit_range):
    if i % 7 == 0:
        continue#infinity loop
    print(i)
    i += 1