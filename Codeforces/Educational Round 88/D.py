def maxSubArraySum(a,size): 
  
    max_so_far = -40*(10**5)
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    s_e_lst = []
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_so_far <= max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 
            s_e_lst.append((start, end, max_so_far))
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    
    return s_e_lst
  

from sys import stdin, stdout
n = int(input())
nums = list(map(int, input().split()))

s_e_lst = maxSubArraySum(nums, n)

ans = 0
for pair in s_e_lst[::-1]:
    s, e, msf= pair
    if ans >= msf:
        break
    ans = max(ans, msf - max(nums[s:e+1]))
print(ans)



