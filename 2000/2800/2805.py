n, m = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, max(arr)
answer = 0

while start <= end:
    answer = (start + end) // 2
    arr2 = [0 if x <= answer else (x - answer) for x in arr]
    s = sum(arr2)

    if s >= m:
        start = answer + 1
    else:
        end = answer - 1

print(end)