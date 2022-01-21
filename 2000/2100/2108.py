import sys
from collections import Counter

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)
l = len(arr)

print(round(sum(arr) / l))
print(arr[l // 2])
if len(arr) > 1:
    counter = Counter(arr)
    _c = counter.most_common()[0][1]
    arr2 = [v for v, c in counter.items() if c == _c]
    if len(arr2) > 1:
        print(arr2[1])
    else:
        print(arr2[0])
    print(arr[-1] - arr[0])
else:
    print(arr[0])
    print(0)