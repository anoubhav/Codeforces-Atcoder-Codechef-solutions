# https://codeforces.com/contest/1343/problems

t = int(input())
import math
for _ in range(t):
    n = int(input())

    kmax = math.ceil(math.log(n, 2)) + 2
    for k in range(2, kmax):
        if n%(2**k - 1) == 0:
            print( n//(2**k - 1))
            break

