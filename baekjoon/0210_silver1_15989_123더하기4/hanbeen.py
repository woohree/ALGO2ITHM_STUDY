# n을 1,2,3의 합으로 나타내는 방법의 수
# 먼저, 3을 위주로 계산

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = []
    count = [0] * 3
    while True:
        if n >= 3:
            numbers += str(n - 3)
            n -= 3
            count[2] += 1
        elif n >= 2:
            n -= 2
            count[1] += 1
        elif n == 1:
            count[0] += 1
            n -= 1
        else:
            break

    print(numbers, count)

