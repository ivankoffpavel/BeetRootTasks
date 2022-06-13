# Write a Python program to detect the number of local variables declared in a function.
def local_in_func():
    x = 2
    y = 4
    z = 'papa'
    return x+y
print(local_in_func.__code__.co_nlocals)