a, b, c = map(int, input().split())
_a = 229 * 324
_b = 297 * 420
_c = 210 * 297
print(f"{((_a * a * 2 + _b * b * 2 + _c * c) / 1000000):.6f}")