from pprint import pprint
import sys
sys.stdin = open('M.txt')


def join_and_split(r, c):
    temp_m, temp_s, temp_d = 0, 0, 0
    ball_cnt = len(matrix[r][c])    # 해당 칸에 있는 파이어볼 개수
    for ball in matrix[r][c]:
        temp_m += ball[2]       # 질량의 합
        temp_s += ball[3]       # 속도의 합
        temp_d += ball[4] % 2

    matrix[r][c] = []
    if temp_m // 5 > 0:     # 질량이 0 초과일 때
        d = (0, 2, 4, 6) if temp_d == 0 or temp_d == ball_cnt else (1, 3, 5, 7)
        for i in range(4):
            matrix[r][c].append([r, c, temp_m // 5, temp_s // ball_cnt, d[i]])


def wizard_shark():
    ways = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

    # 배열에 있는 파이어볼을 탐색
    fire_balls = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                for k in range(len(matrix[i][j])):
                    fire_balls.append(matrix[i][j][k])
                matrix[i][j] = []

    # 탐색한 파이어볼을 하나씩 이동하여 배열에 표시
    for ball in fire_balls:
        r, c, m, s, d = ball[0], ball[1], ball[2], ball[3] % N, ball[4]
        # 다음 행
        if 0 <= r + (ways[d][0] * s) < N:
            r = r + (ways[d][0] * s)
        else:
            r = r + (ways[d][0] * s) + N if r + (ways[d][0] * s) < 0 else r + (ways[d][0] * s) - N
        # 다음 열
        if 0 <= c + (ways[d][1] * s) < N:
            c = c + (ways[d][1] * s)
        else:
            c = c + (ways[d][1] * s) + N if c + (ways[d][1] * s) < 0 else c + (ways[d][1] * s) - N

        matrix[r][c].append([r, c, m, ball[3], d])

    # 한 칸에 두 개 이상의 파이어볼이 있을 때
    for i in range(N):
        for j in range(N):
            if len(matrix[i][j]) > 1:
                join_and_split(i, j)


# 배열 길이 N, 파이어볼 개수 M, 이동 횟수 K
N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # 행 r, 열 c, 질량 m, 속력 s, 방향 d
    r, c, m, s, d = map(int, input().split())
    matrix[r - 1][c - 1].append([r - 1, c - 1, m, s, d])

for _ in range(K):
    wizard_shark()

# K번의 이동 후 남아있는 파이어볼 질량의 합 구하기
ans_m = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            for ball in matrix[i][j]:
                ans_m += ball[2]

print(ans_m)
