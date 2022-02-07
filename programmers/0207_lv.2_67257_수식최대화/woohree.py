from ast import expr


def solution(expression):  # 1시간, 포기
    answer = []
    # 6가지 경우의 수 모두 계산해서 answer에 append하고 max로 리턴
    # 숫자랑 연산자랑 분류
    numbers = []
    for n1 in expression.split('-'):
        for n2 in n1.split('+'):
            for n3 in n2.split('*'):
                numbers.append(n3)
    print(numbers)
    ops = []
    for op in expression:
        if not op.isdigit():
            ops.append(op)
    print(ops)
    # 연산자 우선순위 정하기

    
    return answer

print(solution("100-200*300-500+20"	))  # 60420