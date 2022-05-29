
# import os
# print("The current directory is: ",os.getcwd())
# os.chdir(r"F:\pythonProject\Project1")
# print("The changed directory is : ",os.getcwd())
import sys
print(sys.path)
sys.path.append('my/own/path')
sys.path.insert(1,'/my/own/path')
import os
print(os.environ)
os.environ['PYTHONPATH'] = '/my/own/path'
print(os.environ)
print(sys.path)