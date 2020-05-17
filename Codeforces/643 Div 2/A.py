## 22 mins : very slow. Allow made silly mistake of O(k) when k was clearly mentioned as
# ranging till 10**16. Unncessary TLE. Spent too much time deriving a general formula for ak
# given a1 and k.


t = int(input())
for _ in range(t):
    a1, k = map(int, input().split())

    for _ in range(k-1):

        mi = min(str(a1))
        ma = max(str(a1))

        # without condition ; TLE
        if mi == '0':
            break
        
        a1 = a1 + int(mi)*int(ma)
    
    print(a1)
