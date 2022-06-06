import json
from typing import TextIO
with open('222.json','r') as filename:
    data = json.load(filename)
# data = {'pavel':'ivankov'}
x = input('Input name:')
y = input('Input surname:')
data.update({x:y})
with open('222.json','w') as f:
    json.dump(data,f)
with open('222.json','r') as filename:
    a = json.load(filename)
    print(a)
