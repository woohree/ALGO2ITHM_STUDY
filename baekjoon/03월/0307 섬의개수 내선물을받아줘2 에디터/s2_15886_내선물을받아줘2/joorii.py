import sys
sys.stdin = open('M.txt')


def present():
    count = 0

    for n in range(N - 1):
        if gmap[n] == 'E' and gmap[n + 1] == 'W':
            count += 1

    return count


T = int(input())

for tc in range(T):
    N = int(input())
    gmap = list(map(str, input()))

    print(present())
