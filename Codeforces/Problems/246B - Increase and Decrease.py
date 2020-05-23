# 40 mins. Did not think of obvious soluton. 3 submission errors.

## Trick from Editorial
# Note, that you can always get the answer n–1. To get this result you should make first n–1 equal using the last element as the second element in pair of given operation. 

# But after it, the whole array could become equal. It could happen if the sum of array’s elements is divisible by n. So the answer is n–1 or n.

from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

if sum(nums)%n == 0:
    print(n)
else:
    print(n-1)








###### MY SOLN #####
def process(n, nums, mean):
    g, l, ans = [], [], 0
    for num in nums:
        if num>mean: g.append(num)
        elif num<mean: l.append(num)
        else:ans += 1
    
    while l and g:
        se, ge = l.pop(), g.pop()
    
        if mean - se > ge - mean:
            se += (ge-mean)
            ge = mean
            ans += 1
            l.append(se)
        
        elif mean - se < ge - mean:
            ge -= (mean - se)
            se = mean
            ans +=1
            g.append(ge)
        
        else: # both equal
            ans += 2
    
    if not g:
        return(ans)
    else:
        ans += (len(g)-1)
        return (ans)

from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

if sum(nums)//n == sum(nums)/n:
    print(process(n, nums, sum(nums)/n))
else:
    if sum(nums)/n > 0:
        a = process(n, nums, sum(nums)//n)
        b = process(n, nums, 1 + sum(nums)//n)
        print(a if a>b else b)
    else:
        a = process(n, nums, sum(nums)//n)
        b = process(n, nums, 1 + sum(nums)//n)
        c = process(n, nums, -1 + sum(nums)//n)
        print(max(a, b, c))

    


 
