user = set(x for x in range(1, 31))
assignment = set()
for i in range(28):
    n = int(input())
    assignment.add(n)

assignment = list(user - assignment)
assignment.sort()
for i in assignment:
    print(i)