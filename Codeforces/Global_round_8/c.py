from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it

n = int(input())

coords = []

print(7 + 3*(n-1))
coords = [(0, 0), (1, 0), (0, 1), (2, 1), (1, 2), (1, 1), (2, 2)]
for tup in coords:
    print(*tup)

for i in range(2, n+1):
    print(i, i+1)
    print(i+1, i)
    print(i+1, i+1)


