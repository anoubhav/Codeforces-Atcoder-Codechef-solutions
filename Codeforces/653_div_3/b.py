from sys import stdin
from collections import defaultdict as dd
from collections import deque as dq
import itertools as it
from math import sqrt, log, log2
from fractions import Fraction

t = int(input())
for _ in range(t):
    n  = int(input())
    nummoves = 0
    flag = 0
    while n!=1:
        if n%3!=0:
            flag = 1
            break
        if n%6 == 0:
            n //= 6
        else:
            n*=2
        nummoves += 1
    

    if flag: print(-1)
    else: print(nummoves) 

## Intended solution
# If the number consists of other primes than 2 and 3 then the answer is -1. Otherwise, let cnt2 be the number of twos in the factorization of n and cnt3 be the number of threes in the factorization of n. If cnt2>cnt3 then the answer is -1 because we can't get rid of all twos. Otherwise, the answer is (cnt3−cnt2)+cnt3.
def editorial():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        n = int(input())
    
        count3 = 0
        while n % 3 == 0:
            n //= 3
            count3 += 1
        
        count2 = 0
        while n % 2 == 0:
            n //= 2
            count2 += 1
    
        if n != 1 or count2 > count3:
            print(-1)
            continue
    
        print(count3 + (count3 - count2))
