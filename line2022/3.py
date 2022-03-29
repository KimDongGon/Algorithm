def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    remote_d = dict()
    office_d = dict()

    for remote_task in remote_tasks:
        remote_d[remote_task] = True

    for office_task in office_tasks:
        office_d[office_task] = True

    team_d = dict()

    for i, employee in enumerate(employees):
        flag = True
        for e in employee.split(" "):
            if e.isnumeric():
                team = int(e)
            else:
                if not check_remote(remote_d, e):
                    flag = False
        team_d[team] = team_d.get(team, []) + [[i + 1, flag]]

    for num in range(1, num_teams + 1):
        remote = []
        office = []
        for e in team_d[num]:
            if e[1]:
                remote.append(e[0])
            else:
                office.append(e[0])
        if office:
            answer.extend(remote)
        else:
            answer.extend(remote[1:])

    return answer

def check_remote(remote_d, s):
    return remote_d.get(s, False)

# print(solution(3, ["development","marketing","hometask"], ["recruitment","education","officetask"], ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))
# print(solution(2, ["design"], ["building","supervise"], ["2 design","1 supervise building design","1 design","2 design"]))