import sys
sys.stdin = open('M.txt')


# dfs
def get_safe_area(r, c, elev):
    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if not visited[r][c] and matrix[r][c] > elev:
        visited[r][c] = True

        for idx in range(4):
            # 범위 안이면서, 고도가 더 높으면서, 방문한 적 없는 곳
            if 0 <= r + dy[idx] < N and 0 <= c + dx[idx] < N and matrix[r + dy[idx]][c + dx[idx]] > elev and not visited[r + dy[idx]][c + dx[idx]]:
                get_safe_area(r + dy[idx], c + dx[idx], elev)

        # 하나의 이어진 안전영역을 찾은 후
        return 1

    else:
        return 0


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 지도에 존재하는 높이 정보를 저장할 리스트
elevations = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] not in elevations:
            elevations.append(matrix[i][j])

# 디폴트 안전영역 개수 1
max_cnt = 1
for elevation in elevations:
    temp_cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_cnt += get_safe_area(i, j, elevation)

    if max_cnt < temp_cnt:
        max_cnt = temp_cnt

print(max_cnt)
