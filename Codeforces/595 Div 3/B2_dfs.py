# gives RE
def dfsRecursion(node, cclist, curr):
    cclist[node] = curr
    for nbr in g[node]:
        if cclist[nbr]==0:
            dfsRecursion(nbr, cclist, curr)

# Using DFS
def dfsIteration(node, cclist, curr):
    stack = [node]
    while stack:
        node = stack.pop()
        cclist[node] = curr
        for nbr in g[node]:
            if cclist[nbr] == 0:
                stack.append(nbr)


from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, Counter
# setrecursionlimit(2*10**5 + 10**4)

q = int(input())
for _ in range(q):
    n = int(input())
    nums = list(map(int, stdin.readline().strip().split()))

    
    g = [[] for _ in range(len(nums)+1)]

    for i, pi in enumerate(nums):
        g[i+1].append(pi)

    cclist = [0]*(n+1)

    curr = 1
    for i in nums:
        if cclist[i] == 0:
            dfsIteration(i, cclist, curr)
            curr += 1

    freq = Counter(cclist[1:])

    print(*[freq[cclist[i]] for i in nums])