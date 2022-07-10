# Find Big O of this function:
# def do_something(n):
# 	# n: int
# 	# a: dictionary (int -> int)
# 	a = {}
# 	for i in range(0, n):
# 		a[i] = i
# 	for i in range(0, n):
# 		for j in range(0, n):
# 			print a[i] * a[j]
# O(n^2)