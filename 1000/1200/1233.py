s1, s2, s3 = map(int, input().split())
count = [0 for _ in range(s1 + s2 + s3)]
sum = [0 for _ in range(s1 + s2 + s3)]
for i in range(s1):
    for j in range(s2):
        for k in range(s3):
            sum[i + j + k] = i + j + k + 3
            count[i + j + k] += 1

print(sum[count.index(max(count))])