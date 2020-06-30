# This question took me 40 mins, with two submission errors. I took too long to figure out the formula even after figuring out the pattern. I had to implement simulation and compare to check if formula was right. This was not good appraoch. And very slow. I took more time on this than E1.

from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction
import random

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, stdin.readline().split()))

    # n = 1000
    # k = random.randint(1, 10)
    # nums = []
    # for j in range(n): 
    #     nums.append(random.randint(1, 10))


    freq = dd(int)
    maxkey, maxval = -1, 0
    for i in nums:
        t = i%k
        if t!=0:
            freq[k - t] += 1
            if freq[k-t] > maxval:
                maxval = freq[k-t]

    maxkey = 0
    for key in freq:
        if freq[key] == maxval and key > maxkey:
            maxkey = key


    if len(freq) == 0:
        print(0)
        continue
    
    nummoves = (maxval-1)*k + (maxkey + 1)  
    print(nummoves)


    ### Simulation and comparison
    # ans2 = 0
    # while freq:
    #     for x in range(k):
    #         if freq[x]>0:
    #             freq[x] -= 1
    #         if freq[x] == 0:
    #             del freq[x]

    #         ans2 += 1
    #         if not freq:
    #             break

    # if ans2!=nummoves:
    #     print(n, k)
    #     print(ans2, nummoves)
    #     print(nums)
    # print(max(nummoves, 0))



