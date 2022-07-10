# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for retrieving elements
# using square brackets syntax.
lst = ['mama','papa','Mike','Kate','Sara','Masha','Ann','Nikoletta']
it1 = iter(lst)
print(it1)
def get_by_index(iterable,index): #function wich receives an iterable and index to retrieve a value
    num = 0
    for i in iterable:
        if num == index:
            return i
        num+=1
print(get_by_index(it1,4)) # this code work only once correct because the iterator resumes afer 1 result from current position


