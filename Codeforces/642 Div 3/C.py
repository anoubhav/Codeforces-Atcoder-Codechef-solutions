# 10 mins
t = int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print('0')
        continue

    count = 1
    tempn = 1
    ans = 0
    while True:
        numtiles = 4*tempn + 4
        ans += numtiles*count

        tempn += 2
        count += 1

        if tempn == n:
            break
    
    print(ans)