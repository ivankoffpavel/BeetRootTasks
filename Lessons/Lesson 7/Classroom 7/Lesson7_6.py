# Write an address book, using dictionaries, where I can query contact info, insert new contact, delete contact information, exit
# address book program
dict_1 = {}
while True:

    acivity = input('Type q to quit or f to find an info or d to delete info from dict.book or i to insert new info:')
    if acivity == 'q':
        break
    elif acivity == 'f':
        name_dict = input('Input the name to find:')
        if name_dict in dict_1:
            print('The info is:',dict_1[name_dict])

        else:
            print('Name is not in dict!!!')

    elif acivity == 'i':
        name_dict = input('Input the name to insert: ')
        info_dict = input('Input the info to insert: ')
        dict_1[name_dict] = info_dict
    elif acivity == 'd':
        name_del = input('Input the name to del: ')
        del dict_1[name_del]
    else:
        print('Type q to quit!!!')
        print('You input incorrect letter what to do!!!')



