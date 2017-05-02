n = int(input())
k = n // 2
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[k][i] = '*'
    a[i][k] = '*'
    a[i][i] = '*'
    a[n-i-1][i] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))