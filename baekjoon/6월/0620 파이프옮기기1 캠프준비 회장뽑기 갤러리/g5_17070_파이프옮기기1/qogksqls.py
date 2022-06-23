import sys
sys.stdin = open('B.txt')


def dfs(d, r, c):
    global answer

    if r == N-1 and c == N-1:
        answer += 1
        return

    if d == 0:
        if c + 1 < N and matrix[r][c+1] == 0:
            dfs(0, r, c+1)
        if r + 1 < N and c + 1 < N:
            if matrix[r+1][c] + matrix[r][c+1] == 0 + matrix[r+1][c+1] == 0:
                dfs(1, r+1, c+1)
    elif d == 1:
        if c + 1 < N and matrix[r][c+1] == 0:
            dfs(0, r, c+1)
        if r + 1 < N and matrix[r+1][c] == 0:
            dfs(2, r+1, c)
        if r + 1 < N and c + 1 < N:
            if matrix[r+1][c] + matrix[r][c+1] == 0 + matrix[r+1][c+1] == 0:
                dfs(1, r+1, c+1)
    else:
        if r + 1 < N and matrix[r+1][c] == 0:
            dfs(2, r+1, c)
        if r + 1 < N and c + 1 < N:
            if matrix[r+1][c] + matrix[r][c+1] == 0 + matrix[r+1][c+1] == 0:
                dfs(1, r+1, c+1)


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 0: 가로, 1: 대각선, 2: 세로
answer = 0
dfs(0, 0, 1)  # 방향, 행, 열
print(answer)




'''
from collections import deque

def bfs(q):
    ans = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            if now[0] == 0:
                if now[1][1][1] + 1 < N:
                    if matrix[now[1][1][0]][now[1][1][1] + 1] == 0:
                        if now[1][1][0] == N - 1 and now[1][1][1] + 1 == N - 1:
                            ans += 1
                        elif now[1][1][1] + 1 != N - 1:
                            q.append([0, [
                                (now[1][0][0], now[1][0][1] + 1),
                                (now[1][1][0], now[1][1][1] + 1)
                            ]])
                if now[1][1][0] + 1 < N and now[1][1][1] + 1 < N:
                    if matrix[now[1][1][0]][now[1][1][1] + 1] + matrix[now[1][0][0] + 1][now[1][0][1] + 1] + matrix[now[1][1][0] + 1][now[1][1][1] + 1] == 0:
                        if now[1][1][0] + 1 == N - 1 and now[1][1][1] + 1 == N - 1:
                            ans += 1
                        else:
                            q.append([1, [
                                (now[1][0][0], now[1][0][1] + 1),
                                (now[1][1][0], now[1][1][1] + 1),
                                (now[1][0][0] + 1, now[1][0][1] + 1),
                                (now[1][1][0] + 1, now[1][1][1] + 1)
                            ]])
            elif now[0] == 1:
                if now[1][-1][1] + 1 < N:
                    if matrix[now[1][-1][0]][now[1][-1][1] + 1] == 0:
                        if now[1][-1][0] == N - 1 and now[1][-1][1] + 1 == N - 1:
                            ans += 1
                        elif now[1][-1][1] + 1 != N - 1:
                            q.append([0, [
                                (now[1][-1][0], now[1][-1][1]),
                                (now[1][-1][0], now[1][-1][1] + 1)
                            ]])
                if now[1][-1][0] + 1 < N:
                    if matrix[now[1][-1][0] + 1][now[1][-1][1]] == 0:
                        if now[1][-1][0] + 1 == N - 1 and now[1][-1][1] == N - 1:
                            ans += 1
                        elif now[1][-1][0] + 1 != N - 1:
                            q.append([2, [
                                (now[1][-1][0], now[1][-1][1]),
                                (now[1][-1][0] + 1, now[1][-1][1])
                            ]])
                if now[1][-1][0] + 1 < N and now[1][-1][1] + 1 < N:
                    if matrix[now[1][-1][0]][now[1][-1][1] + 1] + matrix[now[1][-1][0] + 1][now[1][-1][1]] + matrix[now[1][-1][0] + 1][now[1][-1][1] + 1] == 0:
                        if now[1][-1][0] + 1 == N - 1 and now[1][-1][1] + 1 == N - 1:
                            ans += 1
                        else:
                            q.append([1, [
                                (now[1][-1][0], now[1][-1][1]),
                                (now[1][-1][0], now[1][-1][1] + 1),
                                (now[1][-1][0] + 1, now[1][-1][1]),
                                (now[1][-1][0] + 1, now[1][-1][1] + 1)
                            ]])
            else:
                if now[1][1][0] + 1 < N:
                    if matrix[now[1][1][0] + 1][now[1][1][1]] == 0:
                        if now[1][1][0] + 1 == N - 1 and now[1][1][1] == N - 1:
                            ans += 1
                        elif now[1][1][0] + 1 != N - 1:
                            q.append([2, [
                                (now[1][0][0] + 1, now[1][0][1]),
                                (now[1][1][0] + 1, now[1][1][1])
                            ]])
                if now[1][1][0] + 1 < N and now[1][1][1] + 1 < N:
                    if matrix[now[1][1][0] + 1][now[1][1][1]] + matrix[now[1][0][0] + 1][now[1][0][1] + 1] + matrix[now[1][1][0] + 1][now[1][1][1] + 1] == 0:
                        if now[1][1][0] + 1 == N - 1 and now[1][1][1] + 1 == N - 1:
                            ans += 1
                        else:
                            q.append([1, [
                                (now[1][0][0] + 1, now[1][0][1]),
                                (now[1][1][0] + 1, now[1][1][1]),
                                (now[1][0][0] + 1, now[1][0][1] + 1),
                                (now[1][1][0] + 1, now[1][1][1] + 1)
                            ]])
    return ans


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 0: 가로, 1: 대각선, 2: 세로
q = deque()
q.append([0, [(0, 0), (0, 1)]])
answer = bfs(q)

print(answer)
'''
