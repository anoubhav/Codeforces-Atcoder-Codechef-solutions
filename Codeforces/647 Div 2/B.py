# 20 mins. Decent.

def my_soln():
    iszero, maxnum= None, 0
    for i in nums:
        if i == 0:
            iszero = True
        if i > maxnum: maxnum = i

    if iszero:
        asf = 10**9
        for i in nums:
            if i!=0:
                possible = True
                for j in nums:
                    if i^j not in nums:
                        possible = False
                        break
                if possible:
                    if i < asf:
                        asf = i
        print(asf if asf!=10**9 else -1)
        
    else:
        asf = 10**9
        for i in range(1, 2*maxnum):
            possible = True
            for j in nums:
                if i^j not in nums:
                    possible = False
                    break
            if possible:
                if i < asf:
                    asf = i
        print(asf if asf!=10**9 else -1)

from sys import stdin, stdout
q = int(input())
for _ in range(q):
    n = int(input())
    nums = set(map(int, stdin.readline().strip().split()))



        