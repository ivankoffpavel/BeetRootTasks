# Custom exception
# Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its functionality to log
# every error message to a file named `logs.txt`. Tips: Use __init__ method to extend functionality for saving messages to file
#
# ```
class Exception:
    msg = 0
    def __init__(self,x,y=0):
        self.y = y
        self.x = x
        try:
            self.y = 12/self.x
        except ZeroDivisionError:
            Exception.msg = 'Zero'
            print(Exception.msg)
class CustomExeption(Exception):
    def __init__(self,msg):
        self.msg = msg
    def write_error(self):
        with open('logs.txt','a') as file:
            file.write(Exception.msg)
            file.close()

inst = Exception(0)
inst1 = CustomExeption(Exception.msg)
inst1.write_error()







