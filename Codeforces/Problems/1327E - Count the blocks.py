n = int(input())

ans = []
MOD = 998244353
for i in range(1, n):
    # No. of blocks of size i: 2*10*9*pow(10, n-i-1, MOD) + 10*9*9*pow(10, n-i-2, MOD)*(n-i-1)
    t = 2*10*9*pow(10, n-i-1, MOD) + 9*9*pow(10, n-i-1, MOD)*(n-i-1)
    ans.append(t%MOD)

ans.append(10)
print(*ans)
