# Correct in pretests, Incorrect after all tests.
# The solution is CORRECT. However, I got TLE (even after Pypy) in test 26 (only available after contest end).

# 40 mins on this. After this I attempted D. 
# This is not good as penalty is deducted for EACH problem with longer passing time.

### The number of edge case fails...was TOO DAMN HIGH. Spent 1.2 hours upsolving.
from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n = int(stdin.readline())
    elist = list(map(int, stdin.readline().strip().split()))
    # elist = list(map(int, input().split()))
    elist.sort()

    g = 0
    i = 0
    while i<n:
        end = i + elist[i] - 1 # index
        if end>=n: break
        if elist[end] == elist[i]: 
            g += 1
            i = end + 1
        else:
            l = elist[i]
            while l!=elist[end]:
                end += 1
                l += 1

                if end>=n:
                    break
            if end>=n:
                break
            else:
                g += 1
                i = end + 1
    print(g)






import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def my_TLE_soln():
    t = int(input())
    from collections import Counter
    for _ in range(t):
        n = int(input())

        elist = get_ints()
        # elist = list(map(int, input().split()))

        if sum(elist) == n:
            print(n)
            continue

        d = Counter(elist)
        ans = 0
        remlst = []
        for i in sorted(d.keys()):
            
            rem = d[i]%i
            q = d[i]//i   # number of sets of items which are all i and of length i. (i...i)

            # 
            ans += q    # add that to the answer as these sets satisfy the property
            d[i] = rem  # some i's are left (fewer than i as modulo)

            if rem!=0:
                remlst += [i]*rem # those which are left are stored in remlst; increasing order

        # The approach above is greedy. Might not yield optimal solution.

        ans2 = 0
        # if no remaining elements you  have an answer
        if remlst !=[]:
            # iterate from the end elements. each iteration k you choose to skip the last k elements in answer
            for i in range(len(remlst)-1, -1, -1):

                if ans2 > i:
                    break
                temp = 0

                # starting from current end in sorted, check if there exists enough elements in remlst to include it. If so, increment the number of groups : temp by 1.
                while i>-1:
                    i -= (remlst[i])
                    if i>=-1: temp += 1

                # for each ending i, store the best ans
                ans2 = max(ans2, temp)
        
        # Add the # of groups from 1st part (i..i)s  + 2nd part: remaining elements.
        print(ans2+ ans)

# works for my handcrafted cases.    
# my_TLE_soln()
