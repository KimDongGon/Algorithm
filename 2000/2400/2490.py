yut = ['E', 'A', 'B', 'C', 'D']
answer = []
for _ in range(3):
    y = list(map(int, input().split()))
    answer.append(yut[y.count(0)])

for _answer in answer:
    print(_answer)