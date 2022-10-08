# 단순한 확률?????

import sys
sys.stdin = open('B.txt')


def robot(n, prob, row, col):
    global answer

    if n == N:
        answer += prob
        return

    for i in range(4):
        if visited[row + moves[i][0]][col + moves[i][1]] == 0 and directions[i] != 0:
            prob *= directions[i] / 100
            visited[row + moves[i][0]][col + moves[i][1]] = 1
            robot(n + 1, prob, row + moves[i][0], col + moves[i][1])
            prob /= directions[i] / 100
            visited[row + moves[i][0]][col + moves[i][1]] = 0


N, *directions = map(int, input().split())

moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

visited = [[0] * (2*N+1) for _ in range(2*N+1)]
visited[N][N] = 1
answer = 0
robot(0, 1, N, N)

print(answer)

# 순열
# def dfs(a, b, i):
#     global check
#     if visited[a][b] == 0:
#         visited[a][b] = 1
#         if i == N:
#             return
#     else:
#         check += 1
#         return
#     if c[i] == 'E':
#         dfs(a, b+1, i+1)
#     elif c[i] == 'W':
#         dfs(a, b-1, i+1)
#     elif c[i] == 'S':
#         dfs(a-1, b, i+1)
#     elif c[i] == 'N':
#         dfs(a+1, b, i+1)
#
#
# N, *directions = map(int, input().split())
#
# new_directions = []
# direction = ['E', 'W', 'S', 'N']
# for d in range(4):
#     if directions[d] != 0:
#         for _ in range(100 // directions[d]):
#             new_directions.append(direction[d])
#
# perm = list(itertools.permutations(new_directions, N))
# perm = list(set(perm))
#
# check = 0
# for c in perm:
#     visited = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
#     dfs(N//2, N//2, 0)
#
# answer = round(1 - check / len(perm), 2)
# print(f'{answer}')
