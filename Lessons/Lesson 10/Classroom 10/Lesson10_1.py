def count_char(text):#function that count chars in input files string
    st2 = open(text)
    str_take = st2.read()
    count_chars = 0
    for i in str_take:
        if i != ' ':
            count_chars +=1
    return count_chars