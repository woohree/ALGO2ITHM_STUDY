import sys
sys.stdin = open('M.txt')


def robot(row, col, prob):
    global idx
    global probability
    # 동 서 남 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 동 - 북 / 서 - 남 중 한 방향으로만 갈 때
    if not (directions[0] and directions[1]) and not (directions[2] and directions[3]):
        probability = 1.0
        return

    visited[row][col] = True

    # N번째 이동을 마쳤을 때
    if idx == N:
        probability += prob
        return

    # N번만큼 반복
    for i in range(4):
        if 0 <= row + dy[i] < 29 and 0 <= col + dx[i] < 29 and not visited[row + dy[i]][col + dx[i]]:
            idx += 1
            robot(row + dy[i], col + dx[i], prob * (directions[i] / 100))
            idx -= 1
            visited[row + dy[i]][col + dx[i]] = False


# 동 서 남 북 확률
N, *directions = map(int, input().split())
visited = [[0 for _ in range(29)] for _ in range(29)]
# N만큼의 횟수를 카운트할 변수 idx, 단순 이동 경로 확률 probability
idx = probability = 0
robot(14, 14, 1.0)
print(probability)
