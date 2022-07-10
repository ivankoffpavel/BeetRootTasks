# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements
# using square brackets syntax.
lst = ['mama','papa','Mike','Kate','Sara','Masha','Ann','Nikoletta']
it1 = iter(lst)
print(it1)
def get_by_index(iterable,index): #function wich receives an iterable and index to retrieve a value
    num = 0
    for i in iterable:
        if index == num:
            print(i)
        num+=1
get_by_index(lst,0)
get_by_index(lst,1)
get_by_index(lst,2)
get_by_index(lst,3)
get_by_index(lst,4)
get_by_index(lst,5)