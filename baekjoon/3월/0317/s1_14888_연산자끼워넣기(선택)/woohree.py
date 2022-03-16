import sys
from itertools import permutations
sys.stdin = open('L.txt')


def get_max_min():                          # 이건 그냥 계산기!
    mmax = -1000000000                      # 범위: -10억 ~ 10억
    mmin = 1000000000
    for ops in ops_perm:
        stack = []
        for i in range(N-1):
            if not i:                       # i가 0인 경우, 스택이 비어있기 때문에 numbers의 첫 인자를 받아옴
                stack.append(numbers[i])
            stack.append(numbers[i+1])      # i+1번째 인자를 받아옴
            if ops[i] == '+':
                a = stack.pop()             # 후입선출이기 때문에, 
                b = stack.pop()
                stack.append(b + a)         # 나중에 pop한 값을 먼저 넣어줘야 순서가 맞음
            elif ops[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif ops[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif ops[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))      # "음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다" 라는 조건 적용한 결과!

        if stack[0] > mmax:                 # max, min 한번에 구한 것도 백트래킹으로 쳐주나요..?
            mmax = stack[0]
        if stack[0] < mmin:
            mmin = stack[0]

    return mmax, mmin


N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
op_numbers = list(map(int, sys.stdin.readline().rstrip().split()))
ops_temp = ['+', '-', '*', '/']
ops = []                                    # 인풋받은 연산자 갯수만큼 곱해서 다시 저장할 리스트 ex) ['+', '+', '-', '-', '*', '/']
i = 0
while i < 4:                                # ops에 연산자 갯수만큼 곱해서 저장!
    ops += op_numbers[i] * [ops_temp[i]]
    i += 1
ops_perm = set(permutations(ops, N-1))      # 내 코드의 유일한 백트래킹 단 하나..! 순열 구한거에서 set함수 적용해서 중복제거
ans = get_max_min()
print(ans[0], ans[1], sep='\n')


