# Write generator show_letters() that will accept some string and yield only letters from this string
def show_letters(str):
    for i in str:
        if i.isalpha():
            yield i
print(list(show_letters('asfdjkl12434')))