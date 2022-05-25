def factorial_recur(num):
	if(num == 1):
		return 1
	else:
		return num * factorial_recur(num-1)

def factorial_iter(num):
	factor = 1

	for i in range(0, num):
		factor*=(num-i)

	return factor	