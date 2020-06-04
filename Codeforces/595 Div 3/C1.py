from sys import stdin, stdout
from math import ceil, log, floor
import bisect
from itertools import chain, combinations

maxN = 10**4

def allGoodNumbers(maxN):
    # SOLN1: Precompute the powers of three upto n (<=10**4) and find all possible subset sums.
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    maxpower = floor(log(maxN, 3))
    # Store all powers of 3 upto maxpower
    powers = [1]
    t = 1
    for i in range(1, maxpower+1):
        t*=3
        powers.append(t)

    # Get all subset sums. total: 2^(length of powers list)
    allsums = []
    for i in powerset(powers):
        allsums.append(sum(i))

    # sort the subset sums.
    allsums.sort()

    q = int(input())
    
    for _ in range(q):
        n = int(input())
        # if n is more than all sums of powers less than 3.
        if n>allsums[-1]:
            print(powers[-1]*3)

        # binary search on sorted list.
        else:
            ind = bisect.bisect_left(allsums, n)
            print(allsums[ind])

# allGoodNumbers(maxN)

# SOLN2: Iterate from n onwards and check if the ternary representation does not contain a 2.
def ternaryRepresentation():
    # O(nq log n): The outer for loop is linear in n. Ternary number contains log(x, 3) digits. This is a O(log n) operation. It happens every single time inside the loop.
    def if_two_not_in_Ternary (n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            if r==2:
                return False
            nums.append(str(r))
        return True
 
    q = int(input())
    
    for _ in range(q):
        n = int(input())

        for num in range(n, 3*n):
            if if_two_not_in_Ternary(num):
                print(num)
                break
        
ternaryRepresentation()
