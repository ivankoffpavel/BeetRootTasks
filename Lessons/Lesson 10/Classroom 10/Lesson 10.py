# Try to raise such types of exceptions: a) ImportError b) KeyValue c) NameError d) ZeroDivisionError
#from data import dev_ten:
# importError
# try:
    from Lesson10_1 import banana
except ImportError:
    print('Such function doesn\'t exist')
raise Exception(ImportError)
# KeyError
countries = {'UK':'London','Ukraine':'Kyiv'}
if countries['uk'] not in countries:
    raise KeyError
#ZerodivisionError
a = int(input('Input a number  not 0: '))
if a == 0:
    raise ZeroDivisionError
print('The equation is:5/a',5/a)
#nameError
a = 1
b = -1
if a+b == 0:
    raise NameError