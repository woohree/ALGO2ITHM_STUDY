import sys, copy
sys.stdin = open('B.txt')

'''
1. cctv 설치된 좌표를 먼저 구함. 좌표와 cctv 의 숫자 입력
2. cctv 번호 별로 moves 들을 정리
3. dfs 로 풀이. cctv 쭉 검사 하고 재귀 돌렸고 deepcopy 로 매번 matrix 복사함
'''


def dfs(i, matrix):
    global my_min

    if i == len(CCTVs):
        temp = 0
        for n in range(N):
            for m in range(M):
                if matrix[n][m] == 0:
                    temp += 1
        my_min = min(my_min, temp)
        return
    cctv = CCTVs[i]
    if cctv[2] == 1:
        for move in moves1:
            r, c = cctv[0], cctv[1]
            r += move[0]
            c += move[1]
            temp_matrix = copy.deepcopy(matrix)
            if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                temp_matrix[r][c] = '#'
            while 1:
                if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                    temp_matrix[r][c] = '#'
                    r += move[0]
                    c += move[1]
                else:
                    break
            dfs(i + 1, temp_matrix)
    elif cctv[2] == 2:
        for moves in moves2:
            temp_matrix = copy.deepcopy(matrix)
            for move in moves:
                r, c = cctv[0], cctv[1]
                r += move[0]
                c += move[1]
                if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                    temp_matrix[r][c] = '#'
                while 1:
                    if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                        temp_matrix[r][c] = '#'
                        r += move[0]
                        c += move[1]
                    else:
                        break
            dfs(i + 1, temp_matrix)
    elif cctv[2] == 3:
        for moves in moves3:
            temp_matrix = copy.deepcopy(matrix)
            for move in moves:
                r, c = cctv[0], cctv[1]
                r += move[0]
                c += move[1]
                if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                    temp_matrix[r][c] = '#'
                while 1:
                    if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                        temp_matrix[r][c] = '#'
                        r += move[0]
                        c += move[1]
                    else:
                        break
            dfs(i + 1, temp_matrix)
    elif cctv[2] == 4:
        for moves in moves4:
            temp_matrix = copy.deepcopy(matrix)
            for move in moves:
                r, c = cctv[0], cctv[1]
                r += move[0]
                c += move[1]
                if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                    temp_matrix[r][c] = '#'
                while 1:
                    if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                        temp_matrix[r][c] = '#'
                        r += move[0]
                        c += move[1]
                    else:
                        break
            dfs(i + 1, temp_matrix)
    elif cctv[2] == 5:
        temp_matrix = copy.deepcopy(matrix)
        for move in moves1:
            r, c = cctv[0], cctv[1]
            r += move[0]
            c += move[1]
            if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                temp_matrix[r][c] = '#'
            while 1:
                if 0 <= r < N and 0 <= c < M and matrix[r][c] != 6:
                    temp_matrix[r][c] = '#'
                    r += move[0]
                    c += move[1]
                else:
                    break
        dfs(i + 1, temp_matrix)


N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

CCTVs = []
for i in range(N):
    for j in range(M):
        if 0 < matrix[i][j] < 6:
            CCTVs.append((i, j, matrix[i][j]))

moves1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
moves2 = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]
moves3 = [
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, 1)],
    [(-1, 0), (0, -1)]
]
moves4 = [
    [(1, 0), (0, 1), (0, -1)],
    [(1, 0), (0, 1), (-1, 0)],
    [(-1, 0), (0, -1), (1, 0)],
    [(-1, 0), (0, -1), (0, 1)],
]

my_min = N * M
dfs(0, matrix)

print(my_min)
