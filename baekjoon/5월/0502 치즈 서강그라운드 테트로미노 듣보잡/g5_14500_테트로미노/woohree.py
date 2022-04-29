import sys
sys.stdin = open('L.txt')


def get_max_sum(r, c, cnt, now_sum):
    global ans

    if ans >= now_sum + cut*(4-cnt):    # python 1등 코드에 있던 백트래킹,
        return                          # 매트릭스에서 가장 큰 값(cut)을 구해, 지금까지 합(now_sum)에 cut*남은 횟수를 더한 값이 최대값과 같거나 작으면 중단

    if cnt == 4:                        # 4번 채우면 종료
        ans = max(ans, now_sum)         # 최대값 갱신
        return

    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < M and not visited[new_r][new_c]:
            if cnt == 2:                # 가운데손가락 모양 만드려면, 두번째 지점에서 한번 더 탐색해야함
                visited[new_r][new_c] = 1
                get_max_sum(r, c, cnt+1, now_sum+mat[new_r][new_c])  # 따라서, 다음 dfs에 현재 지점 좌표를 넘김
                visited[new_r][new_c] = 0
            visited[new_r][new_c] = 1   # 그외, 평범한 dfs
            get_max_sum(new_r, new_c, cnt+1, now_sum+mat[new_r][new_c])
            visited[new_r][new_c] = 0


N, M = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[0]*M for _ in range(N)]
cut = max(map(max, mat))                # 매트릭에서 가장 큰 값
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        get_max_sum(i, j, 1, mat[i][j])
        visited[i][j] = 0
print(ans)