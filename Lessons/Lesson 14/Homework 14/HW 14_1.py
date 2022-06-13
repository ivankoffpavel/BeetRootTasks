# Write a decorator that prints a function with arguments passed to it.NOTE! It should print the function, not the result of
# its execution! For example: "add called with 4, 5


def logger(func):
    def wraper(*args, **kwargs):
        print(func.__name__, "called with",args)
    return wraper


@logger
def add(a, b):
    return a + b

add(4, 5)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(1,2,3,4,5)



