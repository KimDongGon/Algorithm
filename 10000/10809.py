a = input()
arr = [-1] * 26
for i in a:
    if arr[ord(i) - ord('a')] == -1:
        arr[ord(i) - ord('a')] = a.index(i)

for i in arr:
    print(i)