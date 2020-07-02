# Problem A
a = int(input())
print(a + a**2 + a**3)

# Problem B
s = input()
t = input()

count = 0
for i, j in zip(s, t):
    if i!=j:
        count += 1

print(count)