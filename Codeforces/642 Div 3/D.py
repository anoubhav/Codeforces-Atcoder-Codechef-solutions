# Couldn't solve. Made silly mistakes understanding the question. Tried wrong bases on paper.

# Reference: https://www.youtube.com/watch?v=5y5B30nmQJM

import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*n

    # (length, starting position). In python implementation is min Heap. We want to max length subarray and left most of them. Heaps sort first by key then value. To get max length, multiple by -1.

    # initially we have subarray of 0s of length n, starting at 0.
    zerosub = [(-n, 0)]

    # in place, O(n)
    heapq.heapify(zerosub)

    i = 1
    while zerosub:
        # O(log N) operation
        length, start = heapq.heappop(zerosub)
        length *= -1 # convert back to normal

        # left and right indices of zero subarray
        l = start
        r = length + l - 1

        # O(1)
        if length%2==0:
            mid = (l+r-1)//2
            a[mid] = i
        else:
            mid = (l+r)//2
            a[mid] = i
        
        # Push the new zero subarray ranges to heap IF they exist. O(log N)
        if mid - l:
            heapq.heappush(zerosub, (-(mid-l), l))
        if r - mid:
            heapq.heappush(zerosub, (-(r-mid), mid+1))
        
        i += 1
        
    print(*a)
        

        
