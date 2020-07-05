import os
import sys
from io import BytesIO, IOBase
# from collections import defaultdict as dd
# from collections import deque as dq
# import itertools as it
# from math import sqrt, log, log2
# from fractions import Fraction

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        ans = 'YES'
        for r in range(n):
            row = list(map(int, input().split()))
            if (r == 0 and row[0] >= 3) or (r == n-1 and row[0]>=3):
                ans = 'NO'
            elif (r == 0 and row[-1] >= 3) or (r == n-1 and row[-1]>=3):
                ans = 'NO'    
            elif (r!=0 and row[0]>=4) or (r!=0 and row[-1]>=4):
                ans = 'NO'
            else:
                if r==0 or r==n-1:
                    if max(row) > 3:
                        ans = 'NO'
                else:
                    if max(row) > 4:
                        ans = 'NO'
            
        if ans == 'NO':
            print(ans)
        else:
            print(ans)
            good = [[4]*m for _ in range(n)]
            good[0] = [3]*m
            good[n-1] = [3]*m
            good[0][0] = good[0][-1] = good[n-1][0] = good[n-1][-1] = 2
            for i in range(1, n-1):
                good[i][0] = 3
                good[i][-1] = 3
            
            for row in good:
                print(*row)



































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