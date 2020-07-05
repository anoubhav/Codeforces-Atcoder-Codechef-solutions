from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2, ceil, floor
from fractions import Fraction

n, k = map(int, input().split())
l = floor((2*n + k - k**2)/(2*k))
rem = abs(n - ((l + l + k - 1)*(k))//2)
ans = list(range(l, l+k))

ind = k-1
while rem!=0 and ind > 0:
    prev = ans[ind-1]
    if rem > 2*prev - ans[ind]:
        rem -= 2*prev - ans[ind]
        ans[ind] = 2*prev
    else:
        ans[ind] += rem
        rem = 0

    ind -= 1


if rem!=0:
    print('NO')

else:
    for i in range(k-1):
        if (ans[i] < ans[i+1] <= 2*ans[i]) and (ans[i] >= 1):
            continue
        else:
            print('NO')
            exit()

    print('YES')
    print(*ans)