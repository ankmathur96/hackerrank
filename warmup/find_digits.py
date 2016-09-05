n_cases = int(input())
for i in range(n_cases):
    sum, str_n = 0, input()
    n = int(str_n)
    for c in str_n:
        d = int(c)
        if d == 0:
            continue
        if n % d == 0:
            sum += 1
    print(sum)