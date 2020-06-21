from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
from collections import Counter
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    seq = list(map(int, stdin.readline().split()))
    seqpresent = set(seq)

    if m - 1 > n:
        print(-1)
        continue

    ans = m-1
    for i in range(1, m):
        if i not in seqpresent:
            ans = -1
            break
        else:
            seqpresent.remove(i)

    if ans == -1:
        print(-1)
        continue

    if m in seq:
        seqpresent.remove(m)
    
    ans = 0
    cc = Counter(seq)
    for i in range(1, m):
        ans += cc[i]
    for i in seqpresent:
        ans += cc[i]

    print(ans)
    

