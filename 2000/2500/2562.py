a = int(input())
maxValue = a
position = 1
for i in range(2, 10):
    a = int(input())
    if maxValue < a:
        maxValue = a
        position = i
print(maxValue)
print(position)