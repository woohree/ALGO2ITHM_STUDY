import sys
sys.stdin = open('B.txt')

from itertools import permutations
import math


# 계산한 값을 n에 저장
def calculate(a, b, c):
    global n
    if c == '+':
        n = a + b
    elif c == '-':
        n = a - b
    elif c == '*':
        n = a * b
    else:
        # a가 음수일 때는 값을 소수를 올림을 해서 계산
        if a < 0:
            n = math.ceil(((a * (-1)) / b) * (-1))
        # a가 양수일 때는 값을 소수를 버림을 해서 계산
        else:
            n = math.floor(a / b)


# 연산 찾아서 계산
def get_answer(p):
    for j in range(len(p)):
        if p[j] == '+':
            calculate(n, numbers[j+1], '+')
        elif p[j] == '-':
            calculate(n, numbers[j+1], '-')
        elif p[j] == '*':
            calculate(n, numbers[j+1], '*')
        elif p[j] == '/':
            calculate(n, numbers[j+1], '/')


N = int(sys.stdin.readline().rstrip())  # 숫자 개수
numbers = list(map(int, sys.stdin.readline().rstrip().split()))  # 계산할 숫자 리스트
operations = list(map(int, sys.stdin.readline().rstrip().split()))  # [+, -, *, /]의 순서로 각 연산 별 개수가 입력

# 연산들을 순열 돌리기 위해 문자 형식으로 바꿔줌
operation = []
for i in range(4):
    if i == 0:
        operation += operations[i] * '+'
    elif i == 1:
        operation += operations[i] * '-'
    elif i == 2:
        operation += operations[i] * '*'
    else:
        operation += operations[i] * '/'
# perm에 연산들의 순열 저장
perm = list(permutations(operation, N-1))

# 최대 최소 초기 값 정의
my_max = -1000000000
my_min = 1000000000

# perm 을 for 문 돌림
for p in perm:
    n = numbers[0]
    get_answer(p)

    # n에 최대 최소값 저장되어 있으므로 출력
    # 최댓값 찾기
    if my_max < n:
        my_max = n
    # 최솟값 찾기
    if my_min > n:
        my_min = n

print(my_max)
print(my_min)
