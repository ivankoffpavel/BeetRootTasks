# Sum the Digits of a Number in P
a = '123548'

def sum(num):
    res = 0
    for i in a:
        res += int(i)
    return res

r1 = map(sum,a)
print(list(r1)[0])
gen = sum(i for i in a )
print(gen)