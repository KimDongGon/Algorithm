def solution(logs):
    answer = 0
    for log in logs:
        if len(log) > 100:
            answer += 1
        else:
            arr = []
            cnt = 0
            empty = False
            alpha = False
            for l in log.split(" : "):
                for _l in l.split(" "):
                    if checkKey(_l):
                        cnt += 1
                    else:
                        if not checkAlpha(_l):
                            alpha = True
                    if _l == '':
                        empty = True
                    arr.append(_l)
            if len(arr) != 8 or empty or cnt != 4 or alpha:
                answer += 1
    return answer

def checkKey(s):
    return s == 'team_name' or s == 'application_name' or s == 'error_level' or s == 'message'

def checkAlpha(s):
    return all(_s.isalpha() for _s in s)

# print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))
# print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))