# Obviously, 00-group is useless now. So, how to solve the problem? Let's iterate over the number of books we take from 11-group. Let it be cnt. Then we obviously need to take exactly k−cnt books from groups 01 and 10. Among all books in these three groups we have to choose the cheapest ones. To calculate sum of times in each group fast enought, we can sort each group independently and implement **prefix sums** on these arrays. If k−cnt is less than zero or greater than the size of 01 or 10-group for each possible cnt then the answer is -1.

import sys
 
inp = [int(x) for x in sys.stdin.read().split()]; ii = 0
 
n = inp[ii]; ii += 1
k = inp[ii]; ii += 1
 
T = inp[ii + 0: ii + 3 * n: 3]
A = inp[ii + 1: ii + 3 * n: 3]
B = inp[ii + 2: ii + 3 * n: 3]
 
TA = []
TB = []
TAB = []
for i in range(n):
    if A[i] and B[i]:
        TAB.append(T[i])
    elif A[i]:
        TA.append(T[i])
    elif B[i]:
        TB.append(T[i])
 
def cumsummer(A):
    cumsum = [0]
    for a in A:
        cumsum.append(cumsum[-1] + a)
    return cumsum
 
TA.sort()
TB.sort()
TAB.sort()
 
n = len(TA)
m = len(TB)
nm = len(TAB)
 
TA = cumsummer(TA)
TB = cumsummer(TB)
TAB = cumsummer(TAB)
 
time = inf = 10**9 * 2 + 100
 
for x in range(min(k, nm) + 1):
    y = z = k - x
    if n < y or m < z:
        continue
    time = min(time, TAB[x] + TA[y] + TB[z]) 
print(time if time != inf else -1)