a = input()
arr = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
cnt = 0
for i in a:
    cnt += arr[ord(i) - ord('A')]
print(cnt)