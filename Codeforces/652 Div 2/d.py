from sys import stdin
MOD = 10**9 + 7 
dp = [0]*(2 * 10**6  + 1)

a, b, c = 0, 0, 0
for i in range(3, 2 * 10**6  + 1):
    c = (2*a + b + (1 if i%3 == 0 else 0))%MOD
    a, b = b, c 
    dp[i] = c

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print((4*dp[n])%MOD)