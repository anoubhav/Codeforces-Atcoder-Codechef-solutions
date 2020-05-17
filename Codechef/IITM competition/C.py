# Solved only A, B, C.
# Greedy strategy is followed in this question
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    # total games == total wins as no draws
    totwins = n*(n-1)//2

    # AP sum of wins given to first m-1 teams: n-1 + (n-2) + (n-3).. + (n-m+1)
    # Formula: n(a+l)/2

    calc = ((n-1 + n - m + 1)*(m-1))//2
    if calc >= totwins:
        print(0)
        continue
    else:
        # distribute the remaining wins to the n-m+1
        totwins -= calc

    # remaining n-m+1 teams are distributed wins equally
    start = totwins//(n-m+1)
    for ans in range(start, totwins):
        if totwins <= (n-m+1)*ans:
            print(ans)
            break


