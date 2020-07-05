from sys import stdin
import heapq
def isPowerOfTwo(x): 
    return (x and (not(x & (x - 1)))) 
    
n = int(input())
nums = list(map(int, stdin.readline().split()))
nums.sort()

if n == 1:
    print(nums[0]**2)
    exit()

if nums[0] == nums[n-1]:
    print(n*(nums[0]**2))
    exit()

signi = dict()
for i in range(1, 21):
    signi[i] = []

for i, num in enumerate(nums):
    heapq.heappush(signi[num.bit_length()], (num, i))

ans = 0
for ind in range(n-1, 0, -1):
    if isPowerOfTwo(nums[ind] + 1):
        ans += nums[ind]**2
    else:
        curr = nums[ind]
        msk_of_zeros = (curr ^ (2**curr.bit_length()-1))
        bl = msk_of_zeros.bit_length()
        zeros = []
        for pos, val in enumerate(bin(msk_of_zeros)[2:]):
            if val == '1': zeros.append(bl - pos)
        for j in zeros:
            lst = signi[j]
            if len(lst) > 0:
                a, aind = heapq.heappop(lst)
                b = nums[ind]

                nums[aind] = a & b
                nums[ind] = a | b

                if nums[aind]!=0:
                    heapq.heappush(signi[nums[aind].bit_length()], (nums[aind], aind))

        ans += nums[ind]**2

ans += nums[0]**2
print(ans)