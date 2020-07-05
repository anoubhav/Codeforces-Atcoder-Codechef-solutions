# 11 mins. Quite slow. 
# 
# Also, I didn't check the contraints on a, b,c, d<=10**9. And implemented a for linear for loop
# This will obviously go TLE. TLE/WA gives 50 point penalty. This competition in A and B I made 4 submission errors. 
# Which could have easily been avoided.


from sys import stdin, stdout
from math import ceil, floor
t = int(input())
for _ in range(t):
    # n = int(stdin.readline())
    a, b, c, d = list(map(int, stdin.readline().strip().split()))

    tottime = 0

    if b>=a: print(b)

    else:
        a = a-b
        tottime += b
        if d>=c: 
            print(-1)
        
        else:
            ##TLE
            # while a>0:
            #     a -= (c-d)
            #     tottime += c
            # print(tottime)

            tottime += ceil((a/(c-d)))*c
            print(tottime)

