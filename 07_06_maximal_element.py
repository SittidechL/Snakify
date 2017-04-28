a = [int(s) for s in input().split()]
maximum = a[0]
max_i = 0
for i in range(1, len(a)):
    if a[i] > maximum:
        max_i = i
        maximum = a[i]
print(maximum, max_i, end=' ')