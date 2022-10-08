import sys
sys.stdin = open('B.txt')


# [[1, 20], [2, 50], [3, 30], [4, 10], [4, 40], [4, 60], [6, 5]]
# 1  2  3  4  5  6
# 30 50 40 60 5
N = int(sys.stdin.readline().rstrip())
dw = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dw.sort(key=lambda x: x[1], reverse=True)
visited = [0 for _ in range(1001)]

for d, w in dw:
    if visited[d]:
        while d:
            d -= 1
            if not visited[d]:
                visited[d] = w
                break
    else:
        visited[d] = w
visited[0] = 0
print(sum(visited))

'''
# 3% 시간초과
def dfs(day, score, start):
    global max_score
    max_score = max(max_score, score)
    for i in range(start, N):
        if dw[i][0] >= day:
            dfs(day + 1, score + dw[i][1], i + 1)
    return


N = int(sys.stdin.readline().rstrip())
dw = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dw.sort()

max_score = 0
dfs(1, 0, 0)
print(max_score)
'''