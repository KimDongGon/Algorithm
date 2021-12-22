money = int(input())
money = 1000 - money

extra = [500, 100, 50, 10, 5, 1]

answer = 0

for e in extra:
    while money >= 0:
        if money - e >= 0:
            money -= e
            answer += 1
        else:
            break

print(answer)