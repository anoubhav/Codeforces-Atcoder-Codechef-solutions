from sys import stdin, stdout
n, m = map(int, stdin.readline().strip().split())
n1, n2, n3 = map(int, stdin.readline().strip().split())

# edge_list
from collections import defaultdict
g = defaultdict(list)

for _ in range(m):
    u, v = map(int, stdin.readline().strip().split())
    g[u].append(v)
    g[v].append(u)

colors = [None for _ in range(n)]
