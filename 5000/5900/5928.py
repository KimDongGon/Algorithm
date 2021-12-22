d, h, m = map(int, input().split())
minute = (d - 11) *  24 * 60 + (h - 11) * 60 + (m - 11)
print(minute if minute >= 0 else -1)