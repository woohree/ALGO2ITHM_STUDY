import sys
sys.stdin = open('L.txt')


# 미완!! 실패!!
def dfs(r, c, seven):
    global ans, cnt_s, cnt_y
    seven += 1

    if mat[r][c] == 'S':
        cnt_s += 1
    elif mat[r][c] == 'Y':
        cnt_y += 1

    if cnt_y > 3:
        return

    if seven == 7:
        if cnt_s > 3:
            ans += 1
        return




mat = [list(input()) for _ in range(5)]
# print(mat)
ans = 0
visited = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        cnt_s = cnt_y = 0
        dfs(i, j, 0)
print(ans)