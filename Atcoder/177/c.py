n = int(input())
MOD = 10**9 + 7
nums = list(map(int, input().split()))

pref = [0]*n

for i in range(n)[::-1]:
    pref[i] = (pref[i + 1] if i < n - 1 else 0) + nums[i]
    pref[i] %= MOD

ans = 0
for i in range(n - 1):
    ans += (nums[i] * pref[i + 1])%MOD
    ans %= MOD

print(ans)