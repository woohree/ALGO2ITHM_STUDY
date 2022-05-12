import sys
sys.stdin = open('M.txt')


def postfix():
    operators = ['+', '-', '*', '/', '(', ')']
    ops, ans = [], []

    for char in chars:
        # char이 연산자일 때
        # char이 ops[-1]보다 우선순위가 높으면 push
        # ops[-1]이 char의 우선순위보다 작을때까지 pop
        if char in operators:
            if not ops or char == '(':
                ops.append(char)
            elif char in ['+', '-']:
                while ops[-1] not in ['(']:
                    ans.append(ops.pop())
                    if not ops:
                        break
                ops.append(char)
            elif char in ['*', '/']:
                while ops[-1] not in ['(', '+', '-']:
                    ans.append(ops.pop())
                    if not ops:
                        break
                ops.append(char)
            elif char == ')':
                while ops[-1] != '(':
                    ans.append(ops.pop())
                    if not ops:
                        break
                ops.pop()

        else:
            ans.append(char)

    while ops:
        ans.append(ops.pop())

    return ''.join(ans)


chars = list(input())
print(postfix())
