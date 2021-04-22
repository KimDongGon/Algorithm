array = []
cnt = 0
for i in range(0, 10):
    a = int(input())
    if a % 42 not in array:
        array.append(a % 42)
        cnt += 1
print(cnt)