import sys
sys.stdin = open('G.txt')

def dfs(computer):
    global cnt

    visited[computer] = 1

    # 연결되어있지만 감염되지 않았다면 반복
    for i in connected[computer]:
        if not visited[i]:
            dfs(i)
            cnt += 1

# 컴퓨터 개수
n = int(input())

m = int(input())
connected = [[] * n for _ in range(n+1)]

# 양방향 그래프 추가
for _ in range(m):
    pair = list(map(int, input().split()))
    connected[pair[0]].append(pair[1])
    connected[pair[1]].append(pair[0])

visited = [0] * (n+1)
# 바이러스 걸린 컴퓨터 세기
cnt = 0 

dfs(1)
print(cnt)

