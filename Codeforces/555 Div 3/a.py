from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n = int(input())
# n, m = map(int, input().split())
# nums = list(map(int, stdin.readline().split()))
seen = set()
seen.add(n)
while True:
    n += 1
    while n%10 == 0:
        n //= 10

    if n in seen:
        print(len(seen))
        exit()

    seen.add(n)



