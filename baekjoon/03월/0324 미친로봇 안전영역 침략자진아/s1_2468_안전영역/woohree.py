import sys
sys.stdin = open('L.txt')


def get_safety_area(rainfalls):                             # dfs로 강수량보다 높은 높이의 영역에서 이어진 영역 +1
    max_cnt = 1                                             # 최소 높이보다 강수량이 적으면, 이어진 영역은 1
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for rain in rainfalls:                                  # 높이만큼의 강수량만 확인
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for r in range(N):
            for c in range(N):
                news = []                                   # 이하, dfs
                if not visited[r][c] and mat[r][c] > rain:  # 아직 확인하지 않고, 강수량보다 높은 영역만 이어진 영역 확인
                    cnt += 1
                    news.append((r, c))
                while news:
                    now = news.pop()
                    visited[now[0]][now[1]] = 1
                    for move in moves:
                        new_r, new_c = now[0] + move[0], now[1] + move[1]
                        if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c] and mat[new_r][new_c] > rain:
                            visited[new_r][new_c] = 1
                            news.append((new_r, new_c))
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt


N = int(input())
mat = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
rainfalls = set()
for i in range(N):
    for j in range(N):
        rainfalls |= {mat[i][j]}                            # 중복 쳐내면서 확인할 영역 높이만 저장
ans = get_safety_area(rainfalls)
print(ans)