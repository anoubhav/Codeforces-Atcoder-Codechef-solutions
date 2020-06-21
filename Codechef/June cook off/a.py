from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n, b, m = map(int, input().split())
    nums = list(map(int, stdin.readline().split()))

    curr = None
    ans = 0

    for i in nums:
        if not curr:
            block = i//b
            curr = [block*b, block*b + b-1]
            ans += 1
        else:
            if i >= curr[0] and i <= curr[1]:
                pass
            else:
                ans += 1
                block = i//b
                curr = [block*b, block*b + b-1]
        # print(ans, curr)
    print(ans)


