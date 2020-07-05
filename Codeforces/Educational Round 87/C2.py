from sys import stdin, stdout
from math import sin, cos, radians, pi
t = int(input())
for _ in range(t):
    n = int(stdin.readline())

    # embed 2n-gon is square of minimum length. You can rotate 2n-gon and/or the square.

    # circum radius
    s = 1
    R = (s/2)/sin(pi/(4*n))
    print(R)

    # print(2*R*cos(pi/(4*n)))


# https://www.mathopenref.com/polygonradius.html

# https://math.stackexchange.com/questions/3679533/what-is-the-side-length-of-smallest-square-which-can-embed-a-regular-polygon-wit