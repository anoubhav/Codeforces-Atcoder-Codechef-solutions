n = int(input())
lst = list(map(int, input().split()))

ele = n//2

if n%2==0:
    totsum
    1 = 0
    totsum2 = 0
    count = 0
    for i in range(0, n, 2):
        totsum1 += lst[i]
        totsum2 += lst[i+1]

        count += 1
        if count == ele:
            break
    print(max(totsum1, totsum2))
    
else:
    # Greedy approach fails: [10 5 -50 90 100 90 -10]
    lst = [(i, num) for i, num in enumerate(lst)]
    lst = sorted(lst, key = lambda x: x[1], reverse=True)

    totsum = lst[0][1]
    indices = [lst[0][0]]

    for num in lst[1:]:
        if all((num[0]>i+1 or num[0]<i-1) for i in indices):
            indices.append(num[0])
            totsum += num[1]
        if len(indices) == ele:
            break

    print(totsum)
