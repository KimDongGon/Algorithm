answer = 0

def solution(abilities, k):

    abilities.sort()

    solve(abilities, 0, k)

    return answer

def solve(abilities, sum, k):
    a = abilities.copy()
    if not a:
        global answer
        answer = max(answer, sum)
        return
    num1 = 0
    num2 = 0
    if a:
        num1 = a.pop()

    if a:
        num2 = a.pop()

    if k > 0:
        solve(a, sum + num1, k - 1)
    solve(a, sum + num2, k)

# print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))
print(solution([7, 6, 8, 9, 10], 1))