# Time complexity: O(n log n + m*k log k)
from sys import stdin
n = int(stdin.readline())
alist = list(map(int, stdin.readline().split()))
aindlist = sorted([(elem, i) for i, elem in enumerate(alist)], key = lambda x: (-x[0], x[1]))
m = int(stdin.readline())
ans = []
for _ in range(m):
    k, pos = map(int, stdin.readline().split())
    temp = [x[1] for x in aindlist[:k]]
    # klogk for each query
    temp.sort()
    ans.append(alist[temp[pos - 1]])
print(*ans, sep= '\n')







