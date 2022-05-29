# Create a function that concatenate two lists index-wise
list1 = [1,2,4,6,7]
list2 = [1,3,2,1,1,4,5]
conc_list1 = []
def conc_list(a,b):
    len1 = len(list1)
    len2 = len(list2)
    if len1 <= len2:
        for i in range(len(list1)):
            conc_list1.append(list1[i]+list2[i])
    else:
        for i in range(len(list2)):
            conc_list1.append(list1[i] + list2[i])
    print(conc_list1)
conc_list(list1,list2)
