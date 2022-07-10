import json

book = input('Please input the name of phonepook,"Hint:smartbook": ')
if book == 'smartbook':
    while True:
        jscondition = 0  # json condition check


        def seek_mod(search):  # search mode function
            seek_list_2 = []
            for key, value in data.items():
                for i in value:
                    if i == search:
                        seek_list_2.append(key)
            return seek_list_2


        def print_key(list_seek):  # print mode function
            for i in list_seek:
                for key, value in data.items():
                    if i == key:
                        print('Name is:', key, end=' ')
                        for val in value:
                            if val == value[0]:
                                print('surname is:', val, end=' ')
                            elif val == value[1]:
                                print('tel number is:', val, end=' ')
                            elif val == value[2]:
                                print('adress is:', val, end=' ')
                            elif val == value[3]:
                                print('residention is', val, end='\n\n')


        def seek_print_mode_surname(search):  # seek and print function to print res by surname
            count = 0
            for key, value in data.items():
                if key == search:
                    count += 1
                    print(f'{count}. Surname is:{key}', end=' ')
                    for y in value:
                        if y == value[0]:
                            print('name is:', y, end='  ')
                        elif y == value[1]:
                            print('number is:', y, end='  ')
                        elif y == value[2]:
                            print('region is:', y, end='  ')
                        elif y == value[3]:
                            print('street is:', y, end='\n\n')


        def seek_adres(name_adr):
            seek_list = []
            for key, value in data.items():
                for y in value:
                    if y[0:4] == address[0:4]:
                        seek_list.append(key)
                        return seek_list


        def print_dict(arg1):
            count = 0
            if arg1 == []:
                print('Oooops,no name in smartbook!')
            for i in arg1:
                count += 1
                for key, value in arg1.items():
                    if i == key:
                        print(f'{count}. Surname is:{key}', end=' ')
                        for y in value:
                            if y == value[0]:
                                print('name is:', y, end='  ')
                            elif y == value[1]:
                                print('number is:', y, end='  ')
                            elif y == value[2]:
                                print('region is:', y, end='  ')
                            else:
                                print('street is:', y)


        try:
            with open('smartbook.json', 'r') as f:
                data = json.load(f)
        except Exception:
            print('The smartbook is empty right now, you should choose an insert to fill first record!')
        else:
            jscondition = 1
        print('1.Choose the action you want to do, please:', end='       ')
        print('2.To save data and exit phonebook, type "q"')
        print('3.To insert new name, type "i"', end='                    ')
        print('4.To delete an existing name by telephone number, type "d"')
        print('5.To find an existing name by name type "f"', end='       ')
        print('6.To find an existing name by telephone number type "fn"')
        print('7.To find an existing name by surname type "fs', end='    ')
        print('8.To find an existing name by adress type "fa"')
        print('9.To update the record by telephone number type "nu"')
        print('10.To print all phonebook,type "ps"')
        statement = input('Make you choice, please: ')
        if statement == 'q':
            break
        elif statement == 'i':
            if jscondition == 0:
                while True:
                    surname = input('Input your surname: ')
                    if surname.isalpha() == True:
                        break
                    else:
                        print('You have type only letters!!!')
                while True:
                    name = input('Input your name: ')
                    if name.isalpha() == True:
                        break
                    else:
                        print('You have type only letters!!!')
                while True:
                    tel_numb = input('Input your telephone number: ')
                    if tel_numb.isdigit() and len(tel_numb) == 12:
                        break
                    else:
                        print('Number format is incorrect!!!')
                while True:
                    city = input('Input a city or village of your location: ')
                    if city.isalpha() == True:
                        break
                    else:
                        print('Your city has to contain only letters!!!')
                adress = input('Input your street and home/flat number separated by comma: ')
                data = {surname: [name, tel_numb, city, adress]}
                with open('smartbook.json', 'w') as file:
                    json.dump(data, file)
            else:
                with open('smartbook.json') as file:
                    data = json.load(file)
                while True:
                    surname = input('Input your surname: ')
                    if surname.isalpha() == True:
                        break
                    else:
                        print('You have type only letters!!!')
                while True:
                    name = input('Input your name: ')
                    if name.isalpha() == True:
                        break
                    else:
                        print('You have type only letters!!!')
                while True:
                    tel_numb = input('Input your telephone number: ')
                    if tel_numb.isdigit() and len(tel_numb) == 12:
                        break
                    else:
                        print('Number format is incorrect!!!')
                while True:
                    city = input('Input a city or village of your location: ')
                    if city.isalpha() == True:
                        break
                    else:
                        print('Your city has to contain only letters!!!')
                adress = input('Input your street and home/flat number separated by comma: ')
                data.update({surname: [name, tel_numb, city, adress]})
                with open('smartbook.json', 'w') as file:
                    json.dump(data, file)
        elif statement == 'd':
            if jscondition == 0:
                print('Phonebook is empty, you can only insert data!')
            else:
                num_del = input('Input the number to delete: ')
                with open('smartbook.json', 'r') as f:
                    data = json.load(f)
                res = seek_mod(num_del)
                if res == []:
                    print('There is no number in phonebook!')
                else:
                    print('The surname to del is:', [i for i in res])
                    del data[res[0]]
                    with open('smartbook.json', 'w') as file:
                        json.dump(data, file)
        elif statement == 'f':
            if jscondition == 0:
                print('Phonebook is empty, you can only insert data!')
            else:
                name = input('Input the name to seek: ')
                with open('smartbook.json', 'r') as f:
                    data = json.load(f)
                res = seek_mod(name)
                if res == []:
                    print('There is no name in phonebook!')
                else:
                    print_key(res)
        elif statement == 'fn':
            if jscondition == 0:
                print('Phonebook is empty, you can only insert data!')
            else:
                numb = input('Input the number to seek: ')
                with open('smartbook.json', 'r') as f:
                    data = json.load(f)
                res = seek_mod(numb)
                if res == []:
                    print('There is no number in phonebook!', end='\n\n')
                else:
                    print_key(res)
        elif statement == 'fs':
            if jscondition == 0:
                print('Phonebook is empty, you can only insert data!')
            else:
                surname = input('Input the surname to seek: ')
                with open('smartbook.json', 'r') as f:
                    data = json.load(f)
                seek_print_mode_surname(surname)
        elif statement == 'fa':
            if jscondition == 0:
                print('Phonebook is empty, you can only insert data!')
            else:
                address = input('Input the address to seek: ')
                with open('smartbook.json', 'r') as f:
                    data = json.load(f)
                res = seek_adres(address)
                if res == []:
                    print('There is no address in phonebook!')
                else:
                    print_key(res)
        elif statement == 'ps':
            with open('smartbook.json') as file:
                data = json.load(file)
            print_dict(data)
        elif statement == 'nu':
            tel_num_up = input('Input the telephone number to update contact:')
            with open('smartbook.json') as file:
                data = json.load(file)
            res = seek_mod(tel_num_up)
            print_key(res)
            if res == []:
                print('There is no number in phonebook!!!')
            else:
                surname = input('Input the surname to update: ')
                name = input('Input the name to update: ')
                tel_numb = input('Input the number to update: ')
                city = input('Input the city: ')
                adress = input('Input the adress: ')
                data.update({surname: [name, tel_numb, city, adress]})
                print(data)
                with open('smartbook.json', 'w') as file:
                    json.dump(data, file)
        else:
            print('Your choice is incorrect,try again!!!')
else:
    print("Please try again the phonebook is not correct!")
