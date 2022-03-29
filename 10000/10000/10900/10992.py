N = int(input())

arr = []

for i in range(N):
    if i == 0:
        arr.append(' ' * (N - i - 1) + '*')
    elif i == N - 1:
        arr.append('*' * (2 * (i + 1) - 1))
    else:
        arr.append((N - (i + 1)) * ' ' + '*' + ' ' * (2 * i - 1) + '*' )
print('\n'.join(arr))