## A
n = input()
print('Yes' if '7' in n else 'No')

## B
n = int(input())
ans = 0
for i in range(1, n+1):
    if i%3 == 0 or i%5==0:
        pass
    else:
        ans += i
print(ans)

## C
k = int(input())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += gcd(gcd(a, b), c)
print(ans)