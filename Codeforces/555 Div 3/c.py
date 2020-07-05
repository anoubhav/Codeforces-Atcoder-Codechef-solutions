from sys import stdin
from collections import deque as dq

n = int(stdin.readline())
nums = dq(map(int, stdin.readline().split()))
 
ans = ''
seqlast = -1
while len(nums)>1:
    l, r = nums[0], nums[-1]
 
    if seqlast > l and seqlast > r:
        break
    
    elif seqlast < l and seqlast > r:
        ans += 'L'
        nums.popleft()
        seqlast = l
    
    elif seqlast < r and seqlast > l:
        ans += 'R'
        nums.pop()
        seqlast = r
    else:
        # less than both
        if l < r:
            ans += 'L'
            nums.popleft()
            seqlast = l
        else:
            ans += 'R'
            nums.pop()
            seqlast = r
 
if len(nums):
    if nums[0] > seqlast:
        ans += 'L'
 
print(len(ans))
print(ans)