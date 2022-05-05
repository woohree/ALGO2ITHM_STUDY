import sys
sys.stdin = open('G.txt')

# 도시/버스
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

matrix = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    matrix[start-1][end-1] = min(matrix[start-1][end-1], cost)

for n in range(N):
    matrix[n][n] = 0
    for start in range(N):
        for end in range(N):
            if start != end:
                matrix[start][end] = min(matrix[start][n] + matrix[n][end], matrix[start][end])

for row in matrix:
    answer = ' '.join(map(str, row))
    print(answer.replace('inf', '0'))
    #     if col == float('inf'):
    #         answer.append('0')
    #     else:
    #         answer.append(str(col))
    # print(' '.join(answer))