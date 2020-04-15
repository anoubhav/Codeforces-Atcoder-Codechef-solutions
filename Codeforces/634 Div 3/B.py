# https://codeforces.com/contest/1335/problems
# Solved
import random
t  = int(input())
for _ in range(t):
    n, a, b = list(map(int, input().split()))
    alphabets = 'qwertyuiopasdfghjklzxcvbnm'
    chars = alphabets[:b]
    rem = n%b
    quo = n//b
    print(chars*quo + chars[:rem])