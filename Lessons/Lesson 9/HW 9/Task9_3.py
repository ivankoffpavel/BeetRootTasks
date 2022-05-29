from My_mod import count_lines
from My_mod import count_words
from My_mod import count_char
n = int(input("How many text files you want to create? "))
def create_file(a):#function that creates a necessary quantity of txt files
    global i
    i = 1
    while i <= a:
        text_i = str(input('Input the text you want to save in file,please, or type q to quit: '))
        if text_i == 'q':
            break
        r_i = open(f'text_{i}.txt','w')
        r_i.write(text_i)
        r_i.close()
        i +=1
create_file(n)

for k in range(1,i):
    print('L: '+str(count_lines(f'text_{k}.txt')) +' ' + 'W: '+str(count_words(f'text_{k}.txt')) +' ' + 'Ch: '+str(count_char(f'text_{k}.txt')) + ' ' + str(f'text_{k}.txt'))




