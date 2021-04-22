a, b = map(int, input().split())
c = int(input())

hour = a + c // 60
minute = b + c % 60

print((hour + minute // 60) % 24, minute % 60)