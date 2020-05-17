# Editorial: https://drive.google.com/file/d/1dR9XIihARlu4B9IeM0uoc0wvkNkcTM4Y/view?usp=sharing
from sys import stdin

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, k = list(map(int, stdin.readline().strip().split()))
gold = list(map(int, stdin.readline().strip().split()))

g = gold[0]
for bar in gold[1:]:
    g = gcd(g, bar)
    if g==1:
        break

ans = set()
for x in range(1, k):
    ans.add((g*x)%k)

print(len(ans))
print(*ans)





