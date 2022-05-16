# The greeting program.
# Make a program that has your name and the current day of the week stored as separate variables/
# and then prints a message like this:
# “Good day < name >! < day > is a perfect day to learn some python.”
name='Paul'
current_day='Tuesday'
print(f'Good day {name}! {current_day} is a perfect day to learn some python.')
print('Good day {}! {} is a perfect day to learn some python.'.format(name,current_day))
print('Good day %s! %s is a perfect day to learn some python.' %(name,current_day))
