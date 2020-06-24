t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    # n is  the  length of binary string. x is the balance: count of 0 - count of 1
    s = input()
    
    # prefix balance array
    pref = [0]*n
    pref[0] = 1 if s[0] == '0' else -1

    x_found = 0
    # infinite case
    for i in range(n):
        if i>0: 
            pref[i] += pref[i-1] + (1 if s[i] == '0' else -1)
        if pref[i] == x:
            x_found += 1
    
    last = pref[-1]
    if last == 0:
        if x_found:
            print(-1)
        else:
            print(0)
        continue

    ans = x_found + (1 if x == 0 else 0) #empty substring
    ans = 0
    for i in pref:
        if (x - i)%last == 0:
            if (x-i)//last >= 0:
                ans += 1
    print(ans)
