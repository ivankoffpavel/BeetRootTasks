# Produce a list containing the word ‘minus’ if a number in the numbers is < 0, and the word ‘plus’ if
# the number is > 0. Result would look like
# [‘plus’, ’plus’, ‘minus’]
list = [-1,2,3,-5,4,4,-4]
result_list = []
for i in list:
    if i < 0:
        result_list.append('minus')
    else:
        result_list.append('plus')
print(result_list)