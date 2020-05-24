# minimize |max(A) - min(B)|. Let m = max(A) and n = min(B), such that m, n belong to the parent array. All elements of the array <= m, can be placed in list A. And all elements > m, can be placed in list B. This exhausts the entire parent array and is valid for any m. Also, in above argument there are NO constraints on n.

# Thus, we pick (m, n) such that |m-n| is minimum where m, n belong to the array.
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    diff = 10**9 # stores the minimum |m-n|, i.e., the answer
    for i in range(1, n):
        if arr[i] - arr[i-1] < diff:
            diff = arr[i] - arr[i-1]
            
    print(diff)





    