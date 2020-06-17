from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
from collections import Counter
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, stdin.readline().split()))
    evens = n//2 + n%2
    odds = n//2

    e, o, mismatch = 0, 0, 0
    for i in range(n):
        if i%2 == 0:
            if  nums[i]%2 == 0:
                e += 1
            else:
                o += 1
                mismatch += 1
        else:
            if nums[i]%2 == 1:
                o += 1
            else:
                e += 1
                mismatch += 1
    
    if e!=evens and o!=odds:
        print(-1)
    else:
        print(mismatch//2)




# t = int(input())
# n, m = map(int, input().split())
