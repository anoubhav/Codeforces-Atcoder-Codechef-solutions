from math import sqrt, log, log2, exp, ceil, floor

k = int(input())

# 10 characters in CF. Repeat each k^(1/10) times
each = k**0.1

# if fractional, lower bound of repetition
lower = floor(each)

# initially repeat all of them lower bound number of times.
prod1 = lower**10
count = 0

# one by one replace lower with lower + 1 until the product is greater than k
while prod1 < k:
    count += 1
    prod1 //= lower
    prod1 *= (lower + 1)

# lc: lower count, i.e., no. of characters to be repeated lower bound times.
# uc: upper count, i.e., no. of characters to be repeated (lower+1) bound times.
lc = 10 - count
uc = count

counts = [lower]*lc + [lower + 1]*uc

ans = ''
for i, char in enumerate('codeforces'):
    ans += char*counts[i]

print(ans)

