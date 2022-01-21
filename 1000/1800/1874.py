n = int(input())

start = [x for x in range(1, n + 1)]
start = start[::-1]
temp = []
stack = []
end = []

for _ in range(n):
    e = int(input())
    end.append(e)

answer = []
i = 0

while len(temp) != len(end):
    if len(stack) == 0 or stack[-1] != end[i]:
        if len(start) == 0:
            break
        x = start.pop()
        stack.append(x)
        answer.append('+')
    else:
        x = stack.pop()
        i += 1
        temp.append(x)
        answer.append('-')

if len(temp) != len(end):
    print('NO')
else:
    for a in answer:
        print(a)