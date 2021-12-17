a, b = map(int, input().split())
startX = a // 4 - (1 if a % 4 == 0 else 0)
endX = b // 4 - (1 if b % 4 == 0 else 0)
startY = startX * 4 - a + 1
endY = endX * 4 - b + 1

print(abs(endX - startX) + abs(endY - startY))
