# 7:20

import sys
sys.stdin = open('input.txt')


def hanoi(bae, han, been, n):
    if n == 1:
        print(bae, been)
        return

    hanoi(bae, been, han, n-1)
    print(bae, been)
    hanoi(han, bae, been, n-1)


N = int(input())

move = (2 ** N) - 1
print(move)
if N <= 20:
    hanoi(1, 2, 3, N)
