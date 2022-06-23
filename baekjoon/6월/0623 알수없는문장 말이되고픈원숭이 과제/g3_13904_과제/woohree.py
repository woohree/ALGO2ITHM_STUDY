import sys, heapq
sys.stdin = open('L.txt')


N = int(input())
tasks = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(tasks, (-w, d, w))                   # 점수 기준 최대 힙
visited = [0] * (max(tasks, key=lambda x: x[1])[1]+1)   # 과제 한 날 확인
ans = 0
while tasks:
    x, d, w = heapq.heappop(tasks)
    for i in range(d, 0, -1):                           # 과제 할 수 있는지 확인
        if not visited[i]:                              # 할 수 있으면,
            visited[i] = 1                              # 방문도장 쾅
            ans += w                                    # 점수 갱신
            break
print(ans)