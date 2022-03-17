from itertools import permutations
from collections import deque
import sys
sys.stdin = open('M.txt')


def put_operator():
    # 연산자의 가능한 조합 중 중복 제거
    perms = deque(set(permutations(ops, N - 1)))
    min_sum = 10 ** 9
    max_sum = -(10 ** 9)

    for perm in perms:
        nums = deque(numbers[:])
        # 연산자를 하나씩 돌아가면서 계산
        for p in perm:
            n1 = nums.popleft()
            n2 = nums.popleft()
            if p == '+':
                temp = n1 + n2
            elif p == '-':
                temp = n1 - n2
            elif p == '*':
                temp = n1 * n2
            elif p == '/':
                temp = -(-n1 // n2) if n1 < 0 else n1 // n2
            nums.appendleft(temp)

        if nums[0] > max_sum:
            max_sum = nums[0]
        if nums[0] < min_sum:
            min_sum = nums[0]

    print(f'{max_sum}\n{min_sum}')


# 수의 개수
N = int(input())
numbers = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
operators = ['+', '-', '*', '/']
operator_num = list(map(int, input(). split()))
ops = []

for i in range(4):
    ops += operators[i] * operator_num[i]

put_operator()


