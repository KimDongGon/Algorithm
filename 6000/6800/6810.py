s = '9780921418'

answer = 0

for i in range(10):
    if i % 2 == 0:
        answer += int(s[i])
    else:
        answer += int(s[i]) * 3

a = int(input())
b = int(input())
c = int(input())

print(f'The 1-3-sum is {answer + a + b * 3 + c}')