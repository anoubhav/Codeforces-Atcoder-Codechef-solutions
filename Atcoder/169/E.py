# https://codeforces.com/blog/entry/78195: Geothermal editorial

n = int(input())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# O(nlogn)
A.sort()
B.sort()

if n%2 == 1:
    medA, medB = A[n//2], B[n//2]
    
else:
    medA = A[n//2] + A[n//2 - 1]
    medB = B[n//2] + B[n//2 - 1]

print(medB - medA + 1)





