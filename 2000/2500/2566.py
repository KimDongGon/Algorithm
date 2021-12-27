row = 0
column = 0
answer = 0

for i in range(9):
    n = list(map(int, input().split()))
    m = max(n)
    idx = n.index(m)
    if m > answer:
        row = i + 1
        column = idx + 1
        answer = m

print(answer)
print(row, column)