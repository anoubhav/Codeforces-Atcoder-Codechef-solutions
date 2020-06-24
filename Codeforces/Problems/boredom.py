from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

def dp(n, nums):
    # let dp[i] be the maximum score obtained considering only elements in SORTED array less than equal to i.

    # dp[i] = max(include i, not include i). If we include i, we can't include i-1 and i+1. Here, we don't even count i+1 case. So, include i : dp[i-2] + freq[i]*i. Disclude i: dp[i-1]

    nums.sort()
    dp  = [0]*(nums[-1] + 1)

    freq = defaultdict(int)
    for i in nums: freq[i] += 1

    dp[0] = 0
    dp[1] = freq[1]

    for i in range(2, nums[-1] + 1):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i]*i)

    return dp[-1]

print(dp(n, nums))
# Let f[i] be the maximum sum he can get from taking only values less than or equal i. Then clearly f[0] = 0 since he can't take any of the aray elements. For other values of i, there are two possible cases. The first case is that he does not take any values from the array that are equal to i (sometimes it is better to not take them so he doesn't have to delete all occurrences of i+1 and i-1). In this case, f[i] = f[i-1]. If he doesn't take any values equal to i, the maximum sum he gets is no different than the maximum sum when he was only allowed to take values up to i-1. The other case is that he does take all occurrences of the value i (it's never optimal to take some but not all occurrences since he has to delete the other elements either way). In this case, he is not allowed to take any occurrences of i-1 since he has to delete them all, but he does get the benefit of adding i * freq[i] to his score (where freq[i] is the number of occurrences of i in the array). The fact that he has to delete all occurrences of i+1 will be taken care of when calculating f[i] so you don't have to worry about that. So in this case f[i] = i * freq[i] + f[i-2]. So when figuring out f[i], you take whichever of these cases results in a higher result. Here is some pseudo-code (assuming you pre-computed freq[i] for all i up to 100,000):

def greedy(n, nums):
    # wrong answer on 3 3 4 5 4
    nums.sort()
    freq = defaultdict(int)

    for i in nums:
        freq[i]+=i

    temp = sorted(list(freq.items()), key = lambda x: x[1], reverse=True)

    ans = 0
    for k, v in temp:
        if k in freq:
            ans += v
            if k+1 in freq: del freq[k+1]
            if k-1 in freq: del freq[k-1]
    print(ans)
