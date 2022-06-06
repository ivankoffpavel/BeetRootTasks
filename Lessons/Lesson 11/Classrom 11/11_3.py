# Write a Python program to create a new JSON file from an existing JSON file.
import json
string = {'a':11,'b':15,'c':22}
with open('1.json','w') as file:
    json.dump(string,file)
with open('1.json','r') as file1:
    string1 = json.load(file1)
    print(string1)