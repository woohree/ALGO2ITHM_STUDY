import sys
sys.stdin = open('L.txt')


def dfs(r, c):              # 1이고, 방문안했으면 상하좌우돌면서 이어진 단지 갯수 뽑는 dfs
    global cnt
    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < N and 0 <= new_c < N and not visited[new_r][new_c] and mat[new_r][new_c] == '1':
            visited[new_r][new_c] = 1
            cnt += 1
            dfs(new_r, new_c)


N = int(input())
mat = [input() for _ in range(N)]
# print(mat)
visited = [[0]*N for _ in range(N)]
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and mat[i][j] == '1':
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            ans.append(cnt)
print(len(ans))
for i in sorted(ans):
    print(i)