from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

n = int(input())
nums = list(map(int, stdin.readline().split()))
q = int(input())

freq = dd(int)
ssf = 0
for i in nums:
    freq[i]+= 1
    ssf += i

for _ in range(q):
    b, c = map(int, input().split())
    if freq[b] == 0:
        print(ssf)
        continue
    else:
        minus = b*freq[b]
        plus = c*freq[b]
        ssf += (plus - minus)
        freq[c] += freq[b]
        freq[b] = 0
        print(ssf)


