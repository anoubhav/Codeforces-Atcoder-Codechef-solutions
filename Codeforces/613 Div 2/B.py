# 54 mins with 10 submission errors. This was terrible from my side. With 50 point penalty for each wrong submission.
# First time such large number of errors has happened. Be EXPLICIT about the edge cases. It is always safer.


# Editorial solution
def editorial():
    # O(N)
    # Intuition: If there is ANY prefix or suffix sum which is negative/zero, Adel can completely ignore those elements and take the remaining array as the segment. As remaining array has sum ≥ the sum of the whole array. 
    # So, if that's the case, the answer is "NO".

    # Otherwise, all the segments that Adel can choose will have sum < than the sum of the whole array because the elements that are not in the segment will always have a strictly positive sum. So, in that case, the answer is "YES".


    from sys import stdin, stdout
    t = int(input())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().strip().split()))
        flag = 1
        pref = 0

        # Check if any prefix has 0 or negative sum.
        for num in a:
            pref += num
            if pref<=0:
                print('NO')
                flag = 0
                break
        
        # Check if any suffix has 0 or negative sum IFF all prefix were found positive
        if flag:
            suff = 0
            for num in a[::-1]:
                suff += num
                if suff<=0:
                    print('NO')
                    flag = 0
                    break
        
        # If both prefix sum and suffix sum were found positive.
        if flag: 
            print('YES')
            continue


def my_soln():
    # O(n)
    # Variation of Kadane's algorithm with explicit if statements for edge cases.
    from sys import stdin, stdout
    t = int(input())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().strip().split()))

        yas = sum(a)

        if all([i>0 for i in a]):
            print('YES')
            continue

        if a[0]>=yas:
            print('NO')
            continue

        flag = 1
        msf = a[0]
        ans = a[0]

        for num in a[1:]:
            msf = max(msf + num, num)
            ans = max(ans, msf)

            if num >= yas:
                print('NO')
                flag = 0
                break

            if ans>yas:
                print('NO')
                flag = 0
                break            

        if flag: print('YES')
