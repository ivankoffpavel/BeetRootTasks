import os
def count_lines(text): #function that count lines in input file
    st1 = open(text)
    str_num = (len(st1.readlines()))
    return str_num

def count_char(text):#function that count chars in input files string
    st2 = open(text)
    str_take = st2.read()
    count_chars = 0
    for i in str_take:
        if i != ' ':
            count_chars +=1
    return count_chars

def count_words(text):#function that count words in text file
    st3 = open(text)
    str_take = st3.read()
    words = str_take.split()
    count_word = 0
    for i in words:
        count_word +=1
    return count_word






# print(count_lines('text.txt'))
# print(count_char('text.txt'))
# print(count_words('text.txt'))