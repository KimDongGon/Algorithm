n = int(input())
arr = list(map(int, input().split()))
m = 1


def find():
    global m
    count = 1
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            count += 1
        else:
            if count > m:
                m = count
            count = 1
    else:
        if count > m:
            m = count
find()
arr = arr[::-1]
find()
print(m)