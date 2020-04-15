# https://codeforces.com/contest/1335/problems
# Solved

t = int(input())
for _ in range(t):
    num = int(input())
    if num<3: print(0)
    else:
        # My approach
        # if num%2==0: print(num//2 - 1)
        # else: print(num//2)

        # Alternate
        print((num-1)//2)