import sys
from collections import deque
sys.stdin = open('B.txt')


def bfs(n):
    visited = [n]
    q = deque()
    q.append(n)
    count = 0
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            for j in range(len(matrix[x])):
                if matrix[x][j] not in visited:
                    q.append(matrix[x][j])
                    visited.append(matrix[x][j])
        count += 1
        if len(visited) == N:
            break
    return count


N = int(input())
matrix = [[] * (N+1) for _ in range(N+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    matrix[a].append(b)
    matrix[b].append(a)

score = 50
candidates = []
for i in range(1, N + 1):
    temp = bfs(i)
    if score > temp:
        score = temp
        candidates.clear()
        candidates.append(str(i))
    elif score == temp:
        candidates.append(str(i))

print(score, len(candidates))
print(' '.join(candidates))
