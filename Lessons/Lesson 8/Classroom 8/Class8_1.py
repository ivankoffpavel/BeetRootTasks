# Write a function that takes on an input random ints (between 1 and 10) and returns the longest consecutive
# run and the length of that run of elements of the list.
# Ex. 	def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
# 	def task1(1) -> 1, 1
# 	def task1() -> 0, None
# Then create another function which takes on input result of function from the previous step and prints
# Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”
def count1(*args):
    dic1 = {}
    dic2 = dict()
    count = 0
    if len(args) == 1:
        if args[0] == 0:
            print(str(args[0]), ',', None)  # if
        else:
            print(str(args[0]), 1)
    else:
        for i in range(len(args)):
            if args[i] == args[i - 1]:
                count += 1
                dic1[args[i]] = count
            elif args[i] != args[i - 1]:
                count = 1
        for key, value in dic1.items():
            dic2.update({value: key})
        list1 = sorted(dic2)
        big_value = list1.pop()
        number_int = dic2[big_value]
        return big_value, number_int


result = count1(1, 1, 1, 2, 2, 2, 2, 2)


def count_mod(*result):
    print('Longest run is : ' + str(result[0][0]) + ' of integers - ' + str(result[0][1]))


count_mod(result)
