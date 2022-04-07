# 단순한 확률?????

import sys
sys.stdin = open('B.txt')


def robot(row, col, prob):
    global idx, probability
    # 동 서 남 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 동 - 북 / 서 - 남 중 한 방향으로만 갈 때
    if not (directions[0] and directions[1]) and not (directions[2] and directions[3]):
        probability = 1.0
        return

    visited[row][col] = 1

    # N번째 이동을 마쳤을 때
    if idx == N:
        probability += prob
        return

    # N번만큼 반복
    for i in range(4):
        if 0 <= row + dy[i] < 2*N+1 and 0 <= col + dx[i] < 2*N+1 and not visited[row + dy[i]][col + dx[i]]:
            idx += 1
            robot(row + dy[i], col + dx[i], prob * (directions[i] / 100))
            idx -= 1
            visited[row + dy[i]][col + dx[i]] = 0


# 동 서 남 북 확률
N, *directions = map(int, input().split())
visited = [[0] * (2*N+1) for _ in range(2*N+1)]
# N만큼의 횟수를 카운트할 변수 idx, 단순 이동 경로 확률 probability
idx = probability = 0
robot(N, N, 1.0)
print(probability)

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
