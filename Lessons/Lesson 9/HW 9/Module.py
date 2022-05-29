# Task 1
# Imports practice
# Make a directory with 2 modules; make a function in one of them; then import this function in the other module and /
# use that in your script of choice.

from volume_func_mod import cylinder_volume
r = float(input('Input the radius of cilinder: '))
h = float(input('Input the height of cylinder: '))
print('The volume of cylinder is: ',cylinder_volume(r,h))