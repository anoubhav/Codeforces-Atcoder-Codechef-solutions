# https://www.codechef.com/APRIL20B/problems/CARSELL

def get_profit(n, lst):
    # O(N*logN)
    lst = sorted(lst, reverse = True)
    tot_prof = 0
    # Binary search or linear search for N in sorted list.
    day = 0 
    for i, num in enumerate(lst):
        prof = max(num - day, 0)
        if prof == 0: break

        tot_prof += prof
        day += 1

    return tot_prof%1000000007

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        lst = list(map(int, input().split()))
        print(get_profit(n, lst))