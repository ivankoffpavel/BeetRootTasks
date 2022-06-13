# def add_five(x):
#     return x+5
# def do_twice(f):
#     def resulting_func(x):
#         return f(f(x))
#     return resulting_func
# result = do_twice(add_five)
# print(result(5))
def test(word):
    return f'test {word}'
x = test
print(x)
print(x('this'))
del x
print(test)
x = [test,1,2,0]
print(x)