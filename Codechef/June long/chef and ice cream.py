t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    ans = 'YES'

    freq = {5: 0, 10:0, 15:0, 0:10**4}

    for p in prices:
        # two ways to pay the change
        if p == 15:
            # If you have option between 1 10 and 2 5s, always use 1 10 first, as the 5s can do a 10s job not vice-versa.t
            if freq[p-5]:
                freq[p] += 1
                freq[p-5] -= 1
            elif freq[p-10]>1:
                freq[p] += 1
                freq[p-10] -= 2
            else:
                ans = 'NO'
                break
        
        # one way to pay the change
        elif p < 15:
            if freq[p-5]:
                freq[p] += 1
                freq[p-5] -= 1
            else:
                ans = 'NO'
                break
    print(ans)
