# Solved only A, B, C.
# Editorial link: https://drive.google.com/file/d/1dR9XIihARlu4B9IeM0uoc0wvkNkcTM4Y/view?usp=sharing

# Competition link: https://www.codechef.com/TSR22020?order=desc&sortBy=successful_submissions

T = int(input())
ans = []

for _ in range(T):
    lst = list(map(int, input().split()))
    lst = sorted(lst)
    tot = 10**9

    # largest-smallest + inner pair
    if abs(lst[0] + lst[-1] - lst[1] - lst[-2]) < tot:
        tot = abs(lst[0] + lst[-1] - lst[1] - lst[-2])
    
    # largest + remaining three
    if abs(lst[-1] - (lst[0] + lst[1] + lst[2])) < tot:
        tot = abs(lst[-1] - (lst[0] + lst[1] + lst[2]))
    
    ans.append(tot)

for num in ans:
    print(num)

    


