#Write a decorator `arg_rules` that validates arguments passed to the function.A decorator should take 3 arguments:
#max_length: 15 type_: str contains: [] - list of symbols that an argument should contain If some of the rules
#checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
# ```


def arg_rules(type_: type, max_length: int, contains: list):
   def int_func(f):
       def wrapper(name):
            flag_pos = 0
            flag_neg = 0
            list_new = []
            str = f(name).split()
            if len(name) < 15:
                for i in str:
                    for y in contains:
                        if y in i:
                            flag_pos += 1
                        else:
                            flag_neg +=1
            if flag_pos == len(contains):
                for i in str:
                    print(i,end=' ')
                print()
            else:
                print('Is False')
       return  wrapper
   return int_func

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
create_slogan('05@ukr.net')
create_slogan('05*ukr.net')

# assert create_slogan('johndoe05@gmail.com') is False
#
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'