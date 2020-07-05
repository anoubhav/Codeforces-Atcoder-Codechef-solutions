from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
from collections import Counter
import itertools as it
from math import sqrt, log, log2, ceil, floor
from fractions import Fraction
import heapq
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
t = list(map(int, stdin.readline().split()))

b = {}
for num in t:
    b[num] = b.get(num, 0) + 1

ans = []
for i in a:
    found = 0
    for j in range((n-i)%n, n):
        if j in b and b[j] > 0:
            b[j] -= 1
            ans.append((i+j)%n)
            found = 1
            break
    if found:
        continue

    for j in range(0, (n-i)%n):
        if j in b and b[j] > 0:
            b[j] -= 1
            ans.append((i+j)%n)
            found = 1
            break
print(*ans)


