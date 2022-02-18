k = int(input())

arr = []
d = {}

for i in range(6):
    arr.append(list(map(int, input().split())))
    d[arr[i][0]] = d.get(arr[i][0], []) + [arr[i][1]]

idx = [k for k, v in d.items() if len(v) == 2]
idx.sort()
if idx == [1, 4]:
    idx = [4, 1]
elif idx == [2, 3]:
    idx = [3, 2]

val = [v for k, v in d.items() if len(v) == 1]
answer = val[0][0] * val[1][0]

for i in range(6):
    if i == 5:
        if arr[i][0] == idx[0] and arr[0][0] == idx[1]:
            answer -= arr[i][1] * arr[0][1]
            break
    else:
        if arr[i][0] == idx[0] and arr[i + 1][0] == idx[1]:
            answer -= arr[i][1] * arr[i + 1][1]
            break

print(answer * k)