import sys
sys.stdin = open('G.txt')


def solution(N, x, y):
    global number

    # 현재 위치가 원하는 위치면 number 반환
    if x == r and y == c:
        print(int(number))
        exit(0)
    
    # N == 1로 더 이상 쪼갤 수 없을때 number +1
    if N == 1:
        number += 1
        return
    
    # 분할된 부분에 해당이 되지않을때
    if not (x <= r < x+N) or not (y <= c < y+N):
        number += N * N
        return 

    # 재귀적으로 분할
    solution(N / 2, x, y)
    solution(N / 2, x, y + N / 2)
    solution(N / 2, x + N / 2, y)
    solution(N / 2, x + N / 2, y + N / 2)


n, r, c = map(int, input().split())
N = 2 ** n
number = 0
solution(N, 0, 0)
