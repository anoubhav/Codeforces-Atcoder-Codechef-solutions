s = input()
n = 5
ind = 0

string = 'hello'

for i in s:
    if ind < n and i == string[ind]:
        ind += 1

if ind == n:
    print('YES')
else:
    print('NO')
