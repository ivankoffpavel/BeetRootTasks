#when you have a side and a hight of triangle
a=int(input("Enter a triangle hight "))
b=int(input("Enter a triangle side "))
print('The area of triangle',float(a*b/2))
# 1 way when you have three sides of arbitary triangle
while True:
    print("Input data for 1 way")
    a=float(input("Enter a first triangle side "))
    b=float(input("Enter a second triangle side "))
    c=float(input("Enter a third triangle side "))
    p=(a+b+c)/2
    w=(p*(p-a)*(p-b)*(p-c))**0.5
    # print('The area of triangle is ',w)
    # 2 way when you have three sides of arbitary triangle using module math
    import math
    print("Input data for 2 way")
    a=float(input("Enter a first triangle side "))
    b=float(input("Enter a second triangle side "))
    c=float(input("Enter a third triangle side "))
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    # print('The area of triangle is ',s)
    # comparing the results of 2 ways
    if w==s:
        print("The area is true,and s=",w)
    else:
        print("The area is false!!!!!\nChoose input data,and try again!!!")