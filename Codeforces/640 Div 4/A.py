# https://codeforces.com/contest/1352/problems

# 5 mins to solve
t = int(input())
for _ in range(t):
    number = input()
    n = len(number)
    nums = []
    count = 0
    for i, num in enumerate(number):
        if num == '0':
            continue
        count +=1
        nums.append(int(num)*(10**(n - i - 1)))
    
    print(count)
    # print(' '.join([str(i) for i in nums]))
    print(*nums)

