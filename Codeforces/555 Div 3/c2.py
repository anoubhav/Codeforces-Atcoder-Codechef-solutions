from sys import stdin
from collections import deque as dq

n = int(stdin.readline())
nums = dq(map(int, stdin.readline().split()))

ans = ''
seqlast = -1
while len(nums)>1:
    l, r = nums[0], nums[-1]

    if (seqlast >= l and seqlast >= r):
        break
    
    elif seqlast < l and seqlast >= r:
        ans += 'L'
        nums.popleft()
        seqlast = l
    
    elif seqlast < r and seqlast >= l:
        ans += 'R'
        nums.pop()
        seqlast = r

    elif seqlast < r and seqlast < l:
        # less than both
        if l < r:
            ans += 'L'
            nums.popleft()
            seqlast = l
        elif r < l:
            ans += 'R'
            nums.pop()
            seqlast = r
        else: 
            # r == l
            incleft = 1
            incright = 1
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    incleft += 1
                else:
                    break
            for i in range(len(nums)-1, 0, -1):
                if nums[i] < nums[i-1]:
                    incright += 1
                else:
                    break
            if incleft>incright:
                ans += 'L'*incleft
            else:
                ans += 'R'*incright
    
print(len(ans))
print(ans)
exit()

        
if len(nums):
    if nums[0] > seqlast:
        ans += 'L'

print(len(ans))
print(ans)