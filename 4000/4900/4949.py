while True:
    s = input()
    if s == '.':
        break

    stack = []
    for _s in s:
        if _s == '(' or _s == '[':
            stack.append(_s)
        elif _s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif _s == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')