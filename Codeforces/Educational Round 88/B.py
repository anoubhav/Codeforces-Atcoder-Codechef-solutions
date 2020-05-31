from sys import stdin, stdout
t = int(input())
for _ in range(t):
    n, m, x, y = map(int, stdin.readline().split())

    tot = 0
    for row in range(n):
        row = stdin.readline().strip()
        i = 0
        while i < m:
            if row[i] == '*':
                i += 1
                continue
            else:
                if i+1 < m and row[i+1] == '.':
                    tot += min(2*x, y)
                    i += 2
                else:
                    tot += x
                    i += 1
    print(tot)

def discpage():
    t=int(input())
    
    def solve(s):
        f=len(s)
        dp=[0]*(f+1)
        for i in range(f):
            if s[i]=='.':
                dp[i+1]=dp[i]+x
                if i>=1 and s[i-1]=='.':
                    dp[i+1]=min(dp[i+1],dp[i-1]+y)
            else:
                dp[i+1]=dp[i]
        return dp[f]
    
    for i in range(t):
        n,m,x,y=map(int,input().split())
        ans=0;
        for j in range(n):
            ans+=solve(input())
        print(ans)

