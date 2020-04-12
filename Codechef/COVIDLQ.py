# https://www.codechef.com/APRIL20B/problems/COVIDLQ

def is_social_distance(n, lst):
    prev = -1
    for i, num in enumerate(lst):
        if num == 1:
            if prev == -1: 
                prev = i
            else:
                if i<prev+6: 
                    return 'NO'
                else:
                    prev = i            
    
    return 'YES'
                    

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        lst = list(map(int, input().split()))
        print(is_social_distance(n, lst))

