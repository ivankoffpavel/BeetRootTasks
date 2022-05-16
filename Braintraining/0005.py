#The function that convert 'jdfkl' like in example
#example:"J-Dd-Fff-Kkkk-Lllll"
s=input("Input the string from letters  ")
def func(s):
    count=1
    f=''
    for i in s:
        a=i*count
        b=a.title()
        f+=b+'-'
        count+=1
    print(f'"{f[0:(len(f))-1]}"')
func(s)

