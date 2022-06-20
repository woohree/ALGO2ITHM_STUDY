import sys
sys.stdin = open('M.txt')


def movable(r, c, m):
    if m == 0:      # 파이프 위치 ㅡ일 때
        if c + 1 < N and house[r][c + 1] == 0:
            return True
    elif m == 1:    # 파이프 위치 \일 떄
        if r + 1 < N and c + 1 < N and house[r][c + 1] == 0 and house[r + 1][c + 1] == 0 and house[r + 1][c] == 0:
            return True
    elif m == 2:    # 파이프 위치 ㅣ일 때
        if r + 1 < N and house[r + 1][c] == 0:
            return True
    return False


def move_pipe(r, c, m):     # 현재 좌표 r, c 이전 파이프 인덱스 m
    global answer

    if r == N - 1 and c == N - 1:   # 도착지점 도착했을 때
        answer += 1
        return

    for i in range(-1, 2):      # 파이프 양 옆 인덱스 확인
        if 0 <= m + i < 3:      # 다음 파이프
            if movable(r, c, m + i):    # 다음 위치로 파이프 옮길 수 있을 때
                next_r, next_c = r + moves[m + i][0], c + moves[m + i][1]
                move_pipe(next_r, next_c, m + i)


N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
if house[N - 1][N - 1] != 0:        # 도착지점에 도착할 수 없을 때
    print(0)
else:
    moves = ((0, 1), (1, 1), (1, 0))    # ㅡ, \, ㅣ
    answer = 0
    move_pipe(0, 1, 0)
    print(answer)
