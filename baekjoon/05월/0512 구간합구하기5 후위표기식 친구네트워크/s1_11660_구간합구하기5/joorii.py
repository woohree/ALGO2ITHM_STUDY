import sys
sys.stdin = open('M.txt')

# 표의 크기 N, 합을 구해야 하는 횟수 M
N, M = map(int, sys.stdin.readline().split())
# matrix의 상단, 좌측에 모두 0 추가
matrix = [list(0 for _ in range(N + 1))]
matrix.extend([0] + list(map(int, sys.stdin.readline().split())) for _ in range(N))

# (1, 1)부터 누적 합 구하기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        matrix[i][j] = matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]

# 구간 합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1]
    print(ans)
