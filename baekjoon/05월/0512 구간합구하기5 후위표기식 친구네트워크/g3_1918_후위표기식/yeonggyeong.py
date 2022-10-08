import sys
sys.stdin = open('G.txt')

strings = list(sys.stdin.readline().rstrip())

# 우선순위
rank = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, ')' : 0}
alphas, operators = [], []

for s in strings:
    # 알파벳이면 
    if s not in rank.keys():
        alphas.append(s)
    # 닫는 괄호면 여는 괄호가 나올때까지 pop
    elif s == ')':
        while operators:
            if operators[-1] == '(':
                operators.pop()
                break
            else:
                alphas.append(operators.pop())
    elif s == '(':
        operators.append(s)
    # 우선순위 확인
    else:
        while operators and rank[s] <= rank[operators[-1]]:
            alphas.append(operators.pop())
        operators.append(s)
# 남아있는 연산자
alphas.extend(operators[::-1])
print(''.join(alphas))