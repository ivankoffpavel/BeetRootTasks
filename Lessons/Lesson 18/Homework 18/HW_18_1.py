# Task 1
# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the
# constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
import re
class Email:  # self made way
    def __init__(self,email):
        self.email = email
    def validate(self):
        devider = self.email.index('@')
        prefix = []
        lst = ['%','*','#','^','/','0','1','2','3','4','5','6','7','8','9']
        for i in range(0,devider):
            prefix.append(self.email[i])

        domain =[]
        ind_1 = 0
        for i in self.email[devider+1:]:
            domain.append(i)


        for i in range(0,devider):
            if self.email[i] == '#':
                print('Prefix not valid')

        for i in range(0,devider):
            if self.email[i] == '.' and self.email[i+1] == '.':
               print('Prefix is not valid')


        if prefix[0]  == '-' or prefix[0] == '_' or prefix[0] == '.':
            print('Prefix is not valid!')
        elif prefix[-1] == '-' or prefix[-1] == '_':
            print('Prefix is not valid!')
        else:
            print('Prefix is valid!')
        for i in domain[-2:-1]:
            if i in lst or i == '.':
                print("Domain is not valid")
            else:
                print('Domain is valid!')

print('Self-made way, maybe not quite correct')
mail = Email('buk#@gmail.com')
mail.validate()
# regular exprassion way
class EmailValid:
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    def __init__(self,e_mail):
        self.e_mail = e_mail
    def validation(self):
        if re.fullmatch(EmailValid.regex, self.e_mail):
            print("Valid email")
        else:
            print("Invalid email")
print('Another way using regex with re import')

Class_inst = EmailValid('sasha_janke@gmail.com')
Class_inst.validation()


