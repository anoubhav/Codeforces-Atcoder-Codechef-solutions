import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction
def simulateMax(arr):
    endsize = len(arr)
    while endsize!=1:
        stsize = endsize
        newarr = []

        i = 0
        while i < stsize:
            if i+1 < stsize and arr[i] < arr[i+1]:
                newarr.append(arr[i+1]) # key change
                # print(arr[i], arr[i+1], newarr)
                i += 1
            else:
                newarr.append(arr[i])
            i += 1

        arr = newarr
        endsize = len(arr)
        if stsize == endsize:
            break
    print(*arr)
    if endsize!=1:
        return -1
    else:
        return arr[0]

def simulateMin(arr):
    endsize = len(arr)
    while endsize!=1:
        stsize = endsize
        newarr = []

        i = 0
        while i < stsize:
            if i+1 < stsize and arr[i] < arr[i+1]:
                newarr.append(arr[i])
                i += 1
            else:
                newarr.append(arr[i])
            i += 1

        arr = newarr
        endsize = len(arr)
        if stsize == endsize:
            break

    print(*arr)
    if endsize!=1:
        return -1
    else:
        return arr[0]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        mxpos = 0
        mxelt = nums[0]
        for i, elem in enumerate(nums):
            if elem > mxelt:
                mxelt = elem
                mxpos = i
        
        if mxpos == 0:
            print('NO')
        elif mxpos == n-1:
            print('YES')
        else:
            if nums[0] > nums[-1]:
                print('NO')
            else:
                # will the rightside become single digit
                if nums[mxpos + 1] < nums[-1]:
                    print('YES')
                else:
                    print('NO')

            
            # simulate on both sides
            # mxright = simulateMax(nums[mxpos+1:])
            # mileft = simulateMin(nums[:mxpos])

            # print(mxright, mileft)
            # if mxright!=-1 and mileft!=-1 and mxright > mileft:
            #     print('YES')
            # else:
            #     print('NO')
                

        




































# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion
 
if __name__ == "__main__":
    main()