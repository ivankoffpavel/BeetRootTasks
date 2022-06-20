class FirstClass:
    class_attr = 0
    def __init__(self, a, b):
        self.b = b
        self.a = a
    def print(self,temp):
        print(f'a:{self.a},b:{self.b},class_attr:{FirstClass.class_attr}')
        return self.a+self.b,FirstClass(self.a+self.b,self.a+self.b)
x = FirstClass(1,6)
y = FirstClass(2,8)
# print(x.print())
z= x.print(y)
z = z[1]
print(z.a)
print(z.b)
c = y.print(x)
c = c[1]
print(c.a)
print(c.b)
d = c.print(z)
d = d[1]
print(d.a)
print(d.b)