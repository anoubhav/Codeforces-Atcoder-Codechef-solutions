from sys import stdin
a, b = map(int, stdin.readline().split())

ans = [b]
while b>0:
    if b == a:
        ans.append(a)
        break
    if b%2 == 0:
        b >>= 1
        ans.append(b)
    if (b-1)%10 == 0:
        b = (b-1)//10
        ans.append(b)

if b == a:
    print('YES')
    print(len(ans))
    print(*ans[::-1])
else:
    print('NO')



# a, b = map(int, input().split())

# ans = []
# def dfs(a, b, ops):
#     if a == b:
#         ans.append([ops + [a]])
#     if 2*a < b:
#         dfs(2*a, b, ops + [2*a])
#     if 10*a + 1 < b:
#         dfs(10*a + 1, b, ops + [10*a + 1])

# dfs(a, b, [])
# print(ans)

    
