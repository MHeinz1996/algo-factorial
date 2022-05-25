def factorial_recur(num):
	if(num == 1):
		return 1
	else:
		return num * factorial_recur(num-1)

def factorial_iter(num):
	product = 1

	for i in range(0, num):
		product*=(num-i)

	return product	