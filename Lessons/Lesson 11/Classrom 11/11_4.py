# Find an open API, write a simple get request, get jSON and write it to text file and JSON file
# import json
# import requests
# requests.get(https://api.github.com)
import json

smart_book = {'Ivankov':('Pavlo','45454656','Rivne'),'Galaychuk': ('Sasha','546556','Lviv'),'Gladkij':('Ivan','545446','Kiev'),'Gorkun':('Pavlo','5415455','Odessa')}

# smart_book = {'Ivankov':'Pavlo','Galajchuk':'Oleksandr'}
print(type(smart_book))

with open('smtbook2.json','w') as file:
    json.dump(smart_book,file)

# smart = json.dumps(smart_book)
# print(smart)
with open('smtbook2.json','r') as filename:
    data = json.load(filename)
    print(data)



