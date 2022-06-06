# Task
# 1
# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.Then write
# another script that opens myfile.txt, and reads and prints its contents.Run your two scripts from the system command
# line.Does the new file show up in the directory where you ran your scripts? What if you add a different directory path to
# the filename passed to open? Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at
# the end of the string if you want to fully terminate the line in the file.
string  = 'Hello file world!'
def str_in_file(a):
    with open('my file.txt','w') as file:
        file.write(a)
str_in_file(string)
def str_print(file):
    with open(file,'r') as f:
        str = f.read()
    print(str)
str_print('my file.txt')



