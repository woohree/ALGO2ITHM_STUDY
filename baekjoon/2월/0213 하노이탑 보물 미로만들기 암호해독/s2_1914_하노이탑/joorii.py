import sys
sys.stdin = open('input.txt')


def hanoi(a, b, c, n):
    if n == 0:
        return
    hanoi(a, c, b, n - 1)
    print(a, c)
    hanoi(b, a, c, n - 1)


N = int(input())

print(2 ** N - 1)

if N <= 20:
    hanoi(1, 2, 3, N)
