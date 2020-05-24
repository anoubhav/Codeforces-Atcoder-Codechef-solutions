# A pair (x, y) is similar if they have same parity, i.e., x%2 == y%2 OR they are consecutive |x-y| = 1

t = int(input())
for _ in range(t):
    # n is even (given in question, also a requirement to form pairs)
    n = int(input())
    arr = list(map(int, input().split()))

    # There are only two cases: no.of even (and odd) pairs is even OR no.of even (and odd) pairs is odd. [n is even]

    even_pair_count = 0
    for num in arr:
        if num%2 == 0: even_pair_count += 1
    
    if even_pair_count%2==0: # there are even no. of even pairs and odd pairs
        print('YES')
        continue
    else:
        # both (even and odd pairs) are odd. 
        
        # If we can find a SINGLE |x-y| consecutive number pair (one will be even, other odd because consecutive), we can exclude (x, y) from the array. This leaves us with even no. of (even and odd) pairs.

        arr.sort()
        ans = 'NO'
        
        for i in range(1, n):
            if arr[i] - arr[i-1] == 1:
                ans = 'YES'
                break

        print(ans)

