from collections import defaultdict
from sys import stdin, stdout
n = int(input())
alist = list(map(int, stdin.readline().strip().split()))
blist = list(map(int, stdin.readline().strip().split()))

aind = dict()
for i in range(n):
    aind[alist[i]] = i

dist = defaultdict(int)
ans = 0
for j in range(n):
    top = aind[blist[j]]
    bottom = j

    if top>=bottom:
        dist[top - bottom] += 1
        ans = max(ans, dist[top - bottom])
    else:
        dist[top + n - bottom] += 1
        ans = max(ans, dist[top + n - bottom])

print(ans)
        


    
