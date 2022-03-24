from collections import deque
import sys
sys.stdin = open('M.txt')


def invade(first_row, first_col, second_row, second_col):
    global cnt
    global vill_cnt
    global min_cnt

    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 다음에 방문할 곳
    to_visits = deque([[[first_row, first_col], [second_row, second_col]]])

    while to_visits:
        # 시간 1 증가
        cnt += 1
        # 가지치기...? 이전에 찾은 시간보다 더 큰 시간은 계산할 필요 X
        if cnt >= min_cnt:
            return float('INF')
        # 1초에 번져나갈 좌표 리스트
        current = to_visits.popleft()
        # 다음 초에 번져나갈 좌표 저장용
        to_visits.append([])

        for c in current:
            if not visited[c[0]][c[1]]:
                visited[c[0]][c[1]] = True
                # 방문한 좌표가 마을이면 vill_cnt 1 증가
                if matrix[c[0]][c[1]] == 1:
                    vill_cnt += 1
                    # 만일 모든 마을을 다 들렸다면
                    if vill_cnt == len(villages):
                        return cnt
                # 해당 좌표에서 갈 수 있는 다음 좌표를 저장
                for i in range(4):
                    if 0 <= c[0] + dy[i] < N and 0 <= c[1] + dx[i] < M and not visited[c[0] + dy[i]][c[1] + dx[i]]:
                        to_visits[-1].append([c[0] + dy[i], c[1] + dx[i]])


# 세로 N, 가로 M
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

villages = []
# 마을의 개수 카운트
for n in range(N):
    for m in range(M):
        if matrix[n][m]:
            villages.append([n, m])

min_cnt = float('INF')
for n in range(N):
    for m in range(M):
        for x in range(N):
            for y in range(M):
                # 하나라도 마을(1)이거나, 두 좌표가 겹칠 때는 continue
                if matrix[n][m] or matrix[x][y] or (n == x and m == y):
                    continue
                # 방문했던 곳을 저장할 이차원 리스트
                visited = [[False for _ in range(M)] for _ in range(N)]
                # 찾은 마을의 개수, 시간
                vill_cnt = cnt = 0
                # n, m 은 첫 번째 독주머니의 좌표, x, y는 두 번째 독주머니의 좌표
                temp = invade(n, m, x, y)

                if min_cnt > temp:
                    min_cnt = temp

print(min_cnt - 1)
