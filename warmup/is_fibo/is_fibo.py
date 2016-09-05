from math import sqrt
def is_perfect_square(n):
	root = round(sqrt(n), 0)
	print(n,root)
	return (root ** 2) == n
def is_fib(n):
	return is_perfect_square(5*(n**2) + 4) or is_perfect_square(5*(n**2) - 4)
i = open('input09.txt', 'r')
o = open('output09.txt','r')
n_cases = int(i.readline())
for index in range(n_cases):
	n, expected = int(i.readline()), o.readline()
	if is_fib(n):
		if expected != "isFibo":
			print(n, expected)
	else:
		if expected != "isNotFibo":
			print(n, expected)

def is_fibo(first, second, n):
    if n == first or n == second:
        return True
    elif second > n:
        return False
    else:
        return is_fibo(second, first+second, n)
n_cases = int(input())
for i in range(n_cases):
    n = int(input())
    if is_fibo(0,1,n):
        print("IsFibo")
    else:
        print("IsNotFibo")