computers = int(input())
l = int(input())
d = dict()
for i in range(l):
    start, end = input().split()
    d[start] = d.get(start, []) + [end]
    d[end] = d.get(end, []) + [start]

answer = []
stack = ['1']

while len(stack) != 0:
    top = stack.pop()
    if top not in answer:
        answer.append(top)
    for node in d[top]:
        if node not in answer:
            stack.append(node)

print(len(answer) - 1)