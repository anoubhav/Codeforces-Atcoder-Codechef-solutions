# Unsolved in competition

# https://codeforces.com/contest/1352/problems

# It was pattern recognition; The test examples had the solution hidden. I could have definitely/easily solved this.

t = int(input())
for _ in range(t):
    number = int(input())

    if number < 4:
        print(-1)
        continue
    ans = []

    last_odd = number - (0 if number%2 else 1)

    while last_odd!=-1:
        ans.append(last_odd)
        last_odd -=2
    
    ans.append(4)
    ans.append(2)

    curr = 6
    while curr <= number:
        ans.append(curr)
        curr += 2

    print(' '.join([str(i) for i in ans]))

    