from collections import deque
import sys
sys.stdin = open('G.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
degrees = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

# 키가 큰 사람 += 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    degrees[b] += 1
    graph[a].append(b)

queue = deque()
# degree가 0이면 비교한 적이 없거나 키가 작다는 뜻
for i in range(1, N+1):
    if degrees[i] == 0:
        queue.append(i)

result = []
while queue:
    student = queue.popleft()
    result.append(student)
    # 추가한 학생이랑 비교한 적이 있는 학생들의 degree -1
    for j in graph[student]:
        degrees[j] -= 1
        if degrees[j] == 0:
            queue.append(j)
print(' '.join(map(str, result)))
