from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
from collections import Counter
import itertools as it
from math import sqrt, log, log2, ceil, floor
from fractions import Fraction

t = int(input())
for _ in range(t):
    s = input()
    ans = ''
    for i in range(0, len(s), 2):
        ans += s[i]
    ans += s[-1]
    print(ans)
# n, m = map(int, input().split())
# nums = list(map(int, stdin.readline().split()))
