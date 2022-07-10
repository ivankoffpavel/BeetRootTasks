# Task 2
# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`, `end`,
# and optional step. Tips: See the documentation for `range` function
l = range(1,10,2)
print(l)
print(list(l))
def in_range(start,end,step):
    lst = []
    while start < end:
        lst.append(start)
        start+=step
    gen = (i for i in lst)
    return gen
in_range(2,10,2)
print(in_range(2,10,2))
for i in in_range(1,5,1):
    print(i)
l1 = []
for i in in_range(2,30,3):
    l1.append(i)
print(l1)