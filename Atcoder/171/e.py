from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n = int(input())
xors = list(map(int, stdin.readline().split()))
nums = []
a1 = 0
for i in xors[1:]:
    a1^= i
nums.append(a1)
for i in xors[1:]:
    nums.append(xors[0]^a1^i)

print(*nums)


# someone else's
# n = int(input())
# a = list(map(int, input().split()))
 
# s = 0
# for i in a:
#     s ^= i
 
# print(' '.join([str(s ^ i) for i in a]))

