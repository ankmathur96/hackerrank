def min_changes(str):
	if str == '':
		return 0
	first, second = 0, len(str)-1
	l1, l2, changes = str[first], str[second], 0
	while first < second:
		if l1 != l2:
			changes += abs(ord(l1)-ord(l2))
		first, second = first+1, second-1
		l1, l2 = str[first], str[second]
	return changes
n_cases = int(input())
for _ in range(n_cases):
	print(min_changes(input()))