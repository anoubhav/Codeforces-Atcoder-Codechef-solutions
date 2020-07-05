from sys import stdin, stdout
from math import sin, cos, radians
t = int(input())
for _ in range(t):
    n = int(stdin.readline())

    # embed 2n-gon is square of minimum length. You can rotate 2n-gon and/or the square.

    # exterior angle of regular poly: 360/n
    ext_angle = 360/(2*n)

    ans = 1

    num_sides_on_base = n - (1 if n%2==0 else 0)

    for i in range(num_sides_on_base//2):
        ans += (2*sin(radians((i+1)*ext_angle)))

    print(ans)