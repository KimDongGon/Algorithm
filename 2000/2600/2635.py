n = int(input())
answer = -1
answer_arr = []
for m in range(n, 0, -1):
    arr = [n, m]
    idx = 1
    while True:
        if arr[idx - 1] - arr[idx] < 0:
            if len(arr) > answer:
                answer_arr = arr
                answer = len(arr)
            break
        arr.append(arr[idx - 1] - arr[idx])
        idx += 1

print(answer)
print(" ".join(map(str, answer_arr)))
