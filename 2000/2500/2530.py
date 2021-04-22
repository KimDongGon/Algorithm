a, b, c = map(int, input().split())
d = int(input())
second = (c + d) % 60
minute = (b + ((c + d) // 60)) % 60
hour = (a + (b + ((c + d) // 60)) // 60) % 24
print(hour, minute, second)