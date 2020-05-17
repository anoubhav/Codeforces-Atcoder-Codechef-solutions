# Editorial link: https://drive.google.com/file/d/1dR9XIihARlu4B9IeM0uoc0wvkNkcTM4Y/view?usp=sharing

# Competition link: https://www.codechef.com/TSR22020?order=desc&sortBy=successful_submissions

T = int(input())
for _ in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    if 1 in lst:
        print('YES')
    else:
        print('NO')