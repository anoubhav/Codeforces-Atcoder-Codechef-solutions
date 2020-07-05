from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n = int(input())
nums = list(map(int, stdin.readline().split()))

allset = set(range(1, n+1))
present = set()


inds = []
for ind, elem in enumerate(nums):
    if elem == 0:
        inds.append(ind+1)
    else:
        present.add(elem)
    
leftover = allset - present
leftover = sorted(list(leftover), reverse=True)

n = len(leftover)
for i in range(n):
    if leftover[i] == inds[i]:
        for j in range(n):
            if j!=i and (leftover[i]!=inds[j] and leftover[j]!=inds[i]):
                leftover[i], leftover[j] = leftover[j], leftover[i]
                break

for i in range(len(inds)):
    nums[inds[i]-1] = leftover[i]

print(*nums)

