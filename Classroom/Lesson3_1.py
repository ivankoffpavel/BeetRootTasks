#просте число
while True:
    a=int(input("Введіть число "))
    i=1
    sign=0
    while i < a:
        i+=1
        if a % i ==0:
            i += 1
            sign+=1
    if sign > 1:
        print('Непросте число')
    else:
        print('Просте число')


