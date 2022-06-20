# Produce a list containing the word ‘minus’ if a number in the numbers is < 0, and the word ‘plus’ if the number is > 0.
# Result would look like [‘plus’, ’plus’, ‘minus’]. Read the input list from file and write result to the same file appending it.
ll = [-2,5,6,8,7]
def con1(list):
    new_l = []
    for i in list:
        if i > 0:
            new_l.append('plus')
        else:
            new_l.append('minus')
    print(new_l)
con1(ll)