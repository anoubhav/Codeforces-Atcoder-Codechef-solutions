s = input()
t = input()

n = len(s)
nt = len(t)

ans = 1000
for i in range(n - nt + 1):
    string = s[i:i + nt]

    count = 0
    for c1, c2 in zip(string, t):
        if c1!=c2: count += 1
    
    ans = min(ans, count)

print(ans)