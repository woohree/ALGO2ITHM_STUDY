import sys
sys.stdin = open('L.txt')


def change_to_post(expression):
    ops = []
    result = []

    for char in expression:
        if char.isalpha():                              # 알파벳은 바로 stack에 추가
            result.append(char)

        elif char == '(':                               # 괄호 열린거 ops에 추가, 최고 우선 순위
            ops.append(char)
        elif char == ')':                               # 괄호 닫히면,
            while ops and ops[-1] != '(':               # 열린거 나올 때까지 남은 ops 뒤부터 추가
                result.append(ops.pop())
            ops.pop()                                   # '(' 남아있을테니까 pop

        elif char in ('*', '/'):                        # 곱하기, 나누기와 같은 우선순위 = 곱하기, 나누기
            while ops and ops[-1] in ('*', '/'):        # 따라서, 같은 우선순위면 계속 추가
                result.append(ops.pop())
            ops.append(char)                            # 지금거 ops에 추가

        else:                                           # 더하기, 빼기는 가장 낮은 우선순위
            while ops and ops[-1] != '(':               # 따라서, 괄호만 아니면 다 추가
                result.append(ops.pop())
            ops.append(char)                            # 지금거 ops에 추가

    while ops:                                          # 남은 애들 추가
        result.append(ops.pop())
    return ''.join(result)


expression = input()
ans = change_to_post(expression)
print(ans)