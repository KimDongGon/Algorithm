n = int(input())
users = []
for i in range(n):
    age, name = input().split()
    users.append([int(age), name])

users = sorted(users, key = lambda x: x[0])

for user in users:
    age, name = user
    print(age, name)