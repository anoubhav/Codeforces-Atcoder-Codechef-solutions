n, k = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7
A.sort()
 
l = 0
r = n - 1
sign = 1  # 1 or -1
ans = 1
if k % 2 == 1:
    ans = A[r]
    r -= 1
    k -= 1
    if ans < 0:
        sign = -1
 
while k:
    x = A[l] * A[l + 1]
    y = A[r] * A[r - 1]
    if x * sign > y * sign:
        ans *= x % MOD
        ans %= MOD
        l += 2
    else:
        ans *= y % MOD
        ans %= MOD
        r -= 2
    k -= 2
 
print(ans)