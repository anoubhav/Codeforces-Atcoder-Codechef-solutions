from sys import stdin, stdout
# you're performing O(N) multiplications using a number with O(N) digits, so the time complexity could potentially be at least O(N2).
# To get around this, we need a slightly smarter approach: multiply the numbers together, and print −1 as soon as our product exceeds 10^18. you need to separately check if the input contains a 0

# It turns out that there's a pretty simple C++ solution. The key idea is that we can easily compute the base-10 logarithm of the answer, using the identity that logA1A2A3⋯AN=logA1+logA2+logA3+⋯+logAN. Then, the product is greater than 10^18 if and only if the logarithm is greater than 18.

n = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split()))

if 0 in nums:
    print(0)
        
elif max(nums)>10**18:
    print(-1)

else:
    ans = 1
    for num in nums:
        ans*=num
        if ans > 10**18:
            ans = -1
            break
    
    print(ans)