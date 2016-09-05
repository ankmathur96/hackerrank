def num_deletions(string):
	index, cur, deletions = 1, string[0], 0
	while index != len(string):
		if cur == string[index]:
			deletions += 1
		else:
			cur = string[index]
		index += 1
	return deletions
#O(n) solution
n_cases = int(input())
for _ in range(n_cases):
	print(num_deletions(input()))