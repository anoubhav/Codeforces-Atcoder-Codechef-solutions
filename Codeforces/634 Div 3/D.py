# https://codeforces.com/contest/1335/problems
# Solved

# My solution
t = int(input())
mat = []
# While iterating each row, I wanted to change a non-9 to a 9 while ensuring I pick an element from each 3x3 box and distinct column. Essentially I tried to replace an element but in a more convoluted manner.

indices = [0, 3, 6, 1, 4, 7, 2, 5, 8]
for _ in range(t):
    for k in range(9):
        temp = input()
        row = [char for char in temp]
        if row[indices[k]]!='9':
            row[indices[k]] = '9'
        else:
            row[indices[k]] = '1'
        mat.append(''.join(row))
    
for row in mat:
    print(row)

# Alternate approach: Change all 2s to 1s
t = int(input())
for _ in range(t):
    for k in range(9):
        temp = input()
        print(temp.replace('2', '1'))