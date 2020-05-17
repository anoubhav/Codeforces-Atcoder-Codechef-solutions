# 27 mins

# I spent 20+ mins on the DP solution, which is correct but tle. But later found a loophole. While computes in O(1)
def my_soln():
    n, s = list(map(int, input().split()))
    if (n-1)<(s-(n-1)) - 1:
        print('YES')
        print(*([1]*(n-1) + [s-(n-1)]))
        print(n)
        exit()

    print('NO')

def dp_TLE_soln():
    n, s = list(map(int, input().split()))
    # possible(x) checks if a subset of the n vector can be used to make x.
    newn = n + 1

    possible = [0]*(s+1)
    possible[0] = 1

    for k in range(1, newn):
        if k < newn - 1:
            num = 1   
        else:
            num = s - (n-1)
        for x in range(s, -1, -1):
            if possible[x]:
                possible[x+num] = 1

    for i in range(n, s+1):
        if possible[i] == 0 and possible[s-i] == 0:
            print('YES')
            print(*([1]*(n-1) + [s-(n-1)]))
            print(i)
            exit()



