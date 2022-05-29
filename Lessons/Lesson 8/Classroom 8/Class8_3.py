# Given a list of integers with duplicate elements in it. Create a function to generate another list, which
# contains only the duplicate elements and returns back to user (also try to use *args)
def take_doubles(*args):
    res_list = []
    dub_list = []
    for i in args:
        if i not in res_list:
            res_list.append(i)
        else:
            dub_list.append(i)
    print('The list of only duplicates: ',dub_list)

take_doubles(1,1,1,2,3,6,7,7,5,4)
