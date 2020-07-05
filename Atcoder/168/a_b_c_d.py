from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2, cos, pi
from fractions import Fraction

n, m = map(int, stdin.readline().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

signposts = [0]*(n+1)

queue = dq([1])

visited = [0]*(n+1)
visited[1] = 1
while queue:
    parent = queue.popleft()
    for children in g[parent]:
        if not visited[children]:
            # print('dbg:', parent, children)
            signposts[children] = parent
            queue.append(children)
            visited[children] = 1

if 0 in signposts[2:]:
    print('No')
else:
    print('Yes')
    print(*signposts[2:], sep='\n')















# t = int(stdin.readline())
# for _ in range(t):
# n, m = map(int, stdin.readline().split())
# nums = list(map(int, stdin.readline().split()))
# n = int(input())
# if n%10 in [2, 4, 5, 7, 9]:
#     print('hon')
# elif n%10 in [0, 1, 6, 8]:
#     print('pon')
# else:
#     print('bon')

# k = int(input())
# s = input()

# ans = s[:k] + ('...' if len(s) > k else '')
# print(ans)

# hrhand, minhand, hr, minut = map(int, stdin.readline().split())

# angmin =360*minut/60
# anghr =360*(hr + minut/60)/12


# totang = abs(angmin - anghr)


# print((hrhand**2 + minhand**2 - 2*hrhand*minhand*cos(totang*pi/180))**0.5)

