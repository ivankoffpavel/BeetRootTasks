
def get_by_index(iterable,index): #function wich receives an iterable and index to retrieve a value
    num = 0
    for i in iterable:
        if num == index:
            return i
        num+=1