from sys import stdin, stdout
from collections import Counter
t = int(input())
ans = []
for _ in range(t):
    n = int(stdin.readline())
    alist = list(map(int, stdin.readline().strip().split()))

    alist.sort()

    curr = 1
    for i, num in enumerate(alist):
        ssf = (i + 1)
        if ssf>=num:
            curr = ssf + 1
    
    ans.append(curr)

print(*ans, sep='\n')


