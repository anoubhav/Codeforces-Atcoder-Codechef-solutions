from sys import stdin
# from collections import deque as dq


t = int(input())
for _ in range(t):

    n = int(input())
    nums = list(map(int, stdin.readline().split()))
    
    start = 0
    count = 0
    while start < n:
        sortcnt = 0
        print(start)
        for i in range(start, n-1):
            if nums[i + 1] > nums[i]:
                sortcnt += 1
            else:
                count += 1
                # nums[i+1] < nums[i]
                if nums[i+1] < nums[0]:
                    nums = nums[i+1:i+2] + nums[:i+1] + nums[i+2:]
                else:
                    nums = nums[:i] + nums[i+1:] + nums[i:i+1]
                start = i
                break
        print(nums)
        if sortcnt == n-1-start:
            break
    print(count)

    


