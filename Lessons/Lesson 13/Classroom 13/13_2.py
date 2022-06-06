# 2. Create a list of dictionaries with name, surname and age of each person.
# Write a python program using lambda function to sort the order of names based on its alphabet sequence.
# Write another program to sort by age. Write result to JSON file.
import json

dicts = [
       {"name": "Tom",  "age": 10},
        {"name": "Mark", "age": 5},
       {"name": "Red", "age": 7},
    {"name": "Dick", "age": 12}
        ]
dicts1 =sorted(dicts,key = lambda i: i['name'])
print(dicts)
dicts2 = sorted(dicts,key = lambda i: i['age'])
print(dicts2)
res =(dicts1,dicts2)
with open('res_sort.json','w') as file:
    json.dump(res,file)
