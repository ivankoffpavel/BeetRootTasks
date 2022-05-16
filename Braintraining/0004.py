#Your task is to make a function that can take any non-negative integer as an argument and return it with its /
# digits in descending order. Essentially, rearrange the digits to create the highest possible number.

num=input("Input several data  ")
def descend_order(num):
    global num1
    num_list=[]
    sorted_num=''
    for i in num:
        num_list.append(i)
        num_list.sort()
        num1=sorted_num.join(num_list)
    return num1
print(descend_order(num))
#boolean to string convert
a=1>2
print(a,type(a))#type< boolean>
a=str(a)
print(a,type(a))#type <string>






