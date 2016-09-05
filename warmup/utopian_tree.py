def determine_height(init, n):
    if n == 0:
        return init
    cur, h = 1, init
    while cur <= n:
        if cur % 2 == 0:
            h = h+1
        else:
            h = 2*h
        cur += 1
    return h
n_cases = int(input())
for i in range(n_cases):
    n = int(input())
    print(determine_height(1, n))