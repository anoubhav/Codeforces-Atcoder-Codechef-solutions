# Did not get in the contest. The key insight is in the end, the optimal solution involves taking X books from the front of A and Y books from the front of B. The intermediate transitions from one stack to another do not matter in the big picture.

from sys import stdin
n, m, k = map(int, stdin.readline().split())
astack = list(map(int, stdin.readline().split()))
bstack = list(map(int, stdin.readline().split()))
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def editorial_twoPointer(N, M, K, a, b):
    a, b = [0], [0]
    for i in range(N):
        a.append(a[i] + A[i])
    for i in range(M):
        b.append(b[i] + B[i])

    ans, j = 0, M
    for i in range(N + 1):
        if a[i] > K:
            break
        while b[j] > K - a[i]:
            j -= 1
        ans = max(ans, i + j)
    
    print(ans)
    
def correctApproach_naiveImplementation(n, m, k, astack, bstack):
    # TLE. Time complexity O(N^2). N<2*10^5. 2.2 seconds

    # max books from A upto which total time <= k.
    tot_time = 0
    maxbooks = 0
    prefix_tot_time_a = [0]

    # O(n) to calculate prefix total time for stack A.
    for i in astack:
        if tot_time + i <= k:
            tot_time += i
            maxbooks += 1
            prefix_tot_time_a.append(tot_time)
        else:
            break

    # remove one book at a time from maxbooks of A. And checking how many more books of B we can take. Find the max configuration of taking X books from front of A and Y books from front of B.

    # O(n) to calculate prefix total time for stack B.
    ans = maxbooks
    prefix_tot_time_b = [bstack[0]]
    for i in bstack[1:]:
        prefix_tot_time_b.append(prefix_tot_time_b[-1] + i)

    # ind1 is the number of books taken from A. This is O(n^2).
    for ind1 in range(maxbooks, -1, -1):
        currmax = ind1
        tot_time = prefix_tot_time_a[ind1]

        # this inner loop is O(N) we are trying to find the max number of books we can take from B linearly. We can use binary search instead.
        for ind2 in range(m):
            if tot_time + prefix_tot_time_b[ind2] <= k:
                currmax += 1
            else:
                break
        ans = max(ans, currmax)
    print(ans)
            
def correctApproach_binarySearch(n, m, k, astack, bstack):
    # Accepted. O(N log M + M). 190 ms
    from bisect import bisect_right
    tot_time = 0
    maxbooks = 0
    prefix_tot_time_a = [0]

    # O(n) to calculate prefix total time for stack A.
    for i in astack:
        if tot_time + i <= k:
            tot_time += i
            maxbooks += 1
            prefix_tot_time_a.append(tot_time)
        else:
            break

    # O(n) to calculate prefix total time for stack B.
    ans = maxbooks
    prefix_tot_time_b = [bstack[0]]
    for i in bstack[1:]:
        prefix_tot_time_b.append(prefix_tot_time_b[-1] + i)

    # ind1 is the number of books taken from A. This is O(n log m).
    for ind1 in range(maxbooks, -1, -1):
        currmax = ind1
        tot_time = prefix_tot_time_a[ind1]

        # remaining time; Binary search on prefix total time on B.
        rem = k - tot_time 
        ind2 = bisect_right(prefix_tot_time_b, x = rem)
        currmax += ind2

        ans = max(ans, currmax)
    print(ans)

def correctApproach_twoPointer(n, m, k, astack, bstack):
    # O(N + M). 150ms
    tot = 0
    pa = []
    for i in astack:
        if tot + i <= k:
            tot += i
            pa += [tot]
        else: break
    
    tot = 0
    pb = []
    for i in bstack:
        if tot + i <= k:
            tot += i
            pb += [tot]
        else: break
    
    l1, l2 = len(pa), len(pb)
    if l1 == 0: print(l2)
    elif l2 == 0: print(l1)
    else:
        i, j = l1-1, 0
        ans = max(l1, l2)
        currmax = (i+1) + (j)
        while i > -1 and j < l2:
            if pa[i] + pb[j] <= k:
                currmax += 1
                j += 1
            else:
                currmax -= 1
                i -= 1
            ans = max(ans, currmax)
        print(ans)
            
# correctApproach_naiveImplementation(n, m, astack, bstack)
# correctApproach_binarySearch(n, m, k, astack, bstack)
# correctApproach_twoPointer(n, m, k, astack, bstack)


########## MY FAILED ATTEMPT IN CONTEST; COULD ONLY GET 10 AC AND 10 WA ################
# Tried greedy approach in various ways which were wrong.


# from sys import stdin
# from collections import deque as dq
# from itertools import zip_longest
# n, m, k = map(int, input().split())
# a = dq(map(int, stdin.readline().split()))
# b = dq(map(int, stdin.readline().split()))

# tot = 0
# count = 0

# i = j = 0
# while i < n and j < m:
#     # pick one line
#     if tot + a[i] + b[j] > k:
#         count1 = 0
#         ssf = tot
#         for ind1 in range(i, n):
#             if a[ind1] + ssf > k:
#                 break
#             else:
#                 ssf += a[ind1]
#                 count1 += 1

#         count2 = 0
#         ssf = tot
#         for ind2 in range(j, m):
#             if b[ind2] + ssf > k:
#                 break
#             else:
#                 ssf += b[ind2]
#                 count2 += 1

#         if count1 > count2:
#             print(count + count1)
#         else:
#             print(count + count2) 
#         exit()

#     # pick from any line 
#     else:
#         if tot + min(a[i], b[j]) > k:
#             break
#         elif a[i] < b[j]:
#             tot += a[i]
#             count += 1
#             i += 1
#         elif b[j] < a[i]:
#             tot += b[j]
#             count += 1
#             j += 1
#         else:
#             count1 = 0
#             for ind1 in range(i, n):
#                 if a[ind1] <= a[i]:
#                     count1 += 1
#                 else:
#                     break
#             count2 = 0
#             for ind2 in range(j, m):
#                 if a[ind2] <= b[j]:
#                     count2 += 1
#                 else:
#                     break
            
#             if count1>count2:
#                 tot += a[i]
#                 i += 1
#             elif count2<count1:
#                 tot += b[j]
#                 j += 1
#             else:
#                 if sum(a[i: min(i + count1 + 1, n)]) < sum(b[j: min(j + count2 + 1, m)]):
#                     tot += a[i]
#                     i += 1
#                 else:
#                     tot += b[j]
#                     j += 1
#             count += 1


# if i == n and j == m:
#     print(count)
# elif i < n:
#     for ind in range(i, n):
#         if tot + a[ind] <= k:
#             count += 1
#             tot += a[ind]
#     print(count)
# elif j < m:
#     for ind in range(j, m):
#         if tot + b[ind] <=k:
#             count += 1
#             tot += b[ind]
#     print(count)




# while tot < k:
#     atop = a[0] if a else 10**10
#     btop = b[0] if b else 10**10

#     # both empty
#     if atop == 10**10 and btop == 10**10:
#         break
    
#     # if adding the minimum crosses k.
#     if tot + min(atop, btop) > k:
#         break
    
#     if tot + atop + b
#     if atop < btop:
#         tot += a.popleft()
#         count += 1
#     elif btop < atop:
#         tot += b.popleft()
#         count += 1
#     else:
#         rema = True
#         for i, j in zip(a, b):
#             if i < j:
#                 rema = True
#                 break
#             elif j < i:
#                 rema = False
#                 break
#             else:
#                 pass
#         if rema:
#             tot += a.popleft()
#             count += 1
#         else:
#             tot += b.popleft()
#             count += 1

