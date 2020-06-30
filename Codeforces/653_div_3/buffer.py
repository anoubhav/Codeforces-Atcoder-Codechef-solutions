import time
import sys

# In Python 3.x, 'print i' should be replaced with print(i, end=' ') because print() in Python 3 has a default prefix end='\n' which prompts the console to flush

## You will not see any output until the script completes, and then all at once you will see 0 1 2 3 4 printed to the screen.
for i in range(5):
    print(i, end=''),
    # sys.stdout.flush()
    time.sleep(1)


for i in range(5):
    print(i, end='\n'), ## or you can uncomment below line. 
    # sys.stdout.flush()
    time.sleep(1)


# https://stackoverflow.com/questions/1450551/buffered-vs-unbuffered-io?noredirect=1&lq=1

# You want unbuffered output when you already have large sequence of bytes ready to write to disk, and want to avoid an extra copy into a second buffer in the middle.

# Buffered output streams will accumulate write results into an intermediate buffer, sending it to the OS file system only when enough data has accumulated (or flush() is requested). This reduces the number of file system calls. 

# buffered output is a net win when performing a large number of small writes. Unbuffered output is generally better when you already have large buffers to send

# A buffer often adjusts timing by implementing a queue (or FIFO) algorithm in memory, simultaneously writing data into the queue at one rate and reading it at another rate.

# Key NOTE: buffered output is a net win when performing a large number of small writes. Unbuffered output is generally better when you already have large buffers to send

# Thus, I want to buffer my output. \n default end argument in print 'flushes' (unbuffers) the output. Thus writing every single time for each test case. raw_input() also flushes the output before reading. The \n issue can be resolved by storing the answers in an array and printing it later for all test cases.

# The raw input issue can be resolved by using stdin.readline() as The implementation of input is that it first flushes and then calls sys.stdin.readline. So to not flush, simply use something like input = sys.stdin.readline

