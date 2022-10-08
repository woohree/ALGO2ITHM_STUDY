import sys
sys.stdin = open('L.txt')


def dfs(r, c, cnt):                 # 그냥 dfs, 문제가 좀 심술이 심함
    global max_cnt                  # 딕셔너리가 리스트보다 인자 찾는게 시간이 더 걸리는 거 같음

    if cnt > max_cnt:
        max_cnt = cnt

    for move in moves:
        new_r, new_c = r + move[0], c + move[1]
        if 0 <= new_r < R and 0 <= new_c < C and not visited_alp_num[mat[new_r][new_c]]:
            visited_alp_num[mat[new_r][new_c]] = 1
            dfs(new_r, new_c, cnt + 1)
            visited_alp_num[mat[new_r][new_c]] = 0


R, C = map(int, input().split())
# mat = [list(input()) for _ in range(R)]
mat = [list(map(lambda a: ord(a) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]
# visited_alp = {}
# for i in range(R):
#     for j in range(C):
#         visited_alp.setdefault(mat[i][j], 0)
visited_alp_num = [0] * 26
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
max_cnt = 0
# visited_alp[mat[0][0]] = 1
visited_alp_num[mat[0][0]] = 1
dfs(0, 0, 1)
print(max_cnt)