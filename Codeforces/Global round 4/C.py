from sys import stdin, stdout
w, h = map(int, stdin.readline().strip().split())
div = 998244353
ans = 1
for i in range(1, w+1):
    ans = (ans*2)%div

for i in range(1, h+1):
    ans = (ans*2)%div

print(ans%div)

def alternate():
    h, w = map(int, input().split())
    print(pow(2, h + w, 998244353))
    