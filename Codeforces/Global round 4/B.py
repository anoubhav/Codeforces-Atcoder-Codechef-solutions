from sys import stdin, stdout
s = stdin.readline().strip()
n = len(s)
wcount = [0]*n # no. of w upto i

for i in range(1, n):
    if s[i] == 'v' and s[i-1] == 'v':
        wcount[i] = wcount[i-1] + 1
    else:
        wcount[i] = wcount[i-1]
# print(wcount)

ans = 0
for i, char in enumerate(s):
    if char == 'o':
        ans += (wcount[i-1]*(wcount[-1] - wcount[i-1]))
print(ans)
        

