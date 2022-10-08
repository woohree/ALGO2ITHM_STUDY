import sys
from collections import deque
sys.stdin = open('B.txt')

'''
처음에는 bfs로만으로 풀었다가 시간초과...
bfs로 풀면 이분탐색을 같이 써야한다는 글 보고 고민해봤는데 안 떠올라서 서치함

1. 다익스트라 식으로 input 값을 bridges 라는 리스트에 저장
2. 다리의 중량 제한을 통과 가능한 중량을 이분탐색으로 찾음.
3. bfs 사용. 현재 중량이 다리를 건너다가 목적지에 도착하면 True를 return, 반대로 목적지에 못 도달하면 False를 return. 
4. True 면 low 에 +1, False 면 high 에 -1 해주면서 low 가 high 보다 커질 때는 찾은 후 high 를 출력
'''


def bfs(m):
    visited[start] = 1
    q = deque()
    q.append(start)

    # 3.
    while q:
        now = q.popleft()
        if now == end:
            return True
        for nx, nc in bridges[now]:
            if visited[nx] == 0 and m <= nc:
                q.append(nx)
                visited[nx] = 1
    return False


N, M = map(int, sys.stdin.readline().rstrip().split())
# 1.
bridges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))

# 2.
start, end = map(int, input().split())
left, right = 1, 1000000000
while left <= right:
    visited = [0 for _ in range(N + 1)]
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)
'''
N, M = map(int, sys.stdin.readline().rstrip().split())
bridges = [0] * (N+1)
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    if bridges[A] == 0:
        bridges[A] = [[B, C, str(A)]]
        if bridges[B] == 0:
            bridges[B] = [[A, C, str(B)]]
        else:
            bridges[B].append([A, C, str(B)])
    else:
        bridges[A].append([B, C, str(A)])
        if bridges[B] == 0:
            bridges[B] = [[A, C, str(B)]]
        else:
            bridges[B].append([A, C, str(B)])
one, other = map(int, sys.stdin.readline().rstrip().split())


def bfs():
    global my_max

    while islands:
        current = islands.popleft()
        if my_max >= current[1]:
            continue
        nc = current[0]
        if str(nc) not in current[2]:
            current[2] += str(nc)
            for b in bridges[nc]:
                if my_max >= b[1]:
                    continue
                islands.append(b[:])
                islands[-1][1] = min(islands[-1][1], current[1])
                islands[-1][2] = current[2]
                if b[0] == other:
                    my_max = max(my_max, islands[-1][1])
                    islands.pop()
                    continue
    return


islands = deque()
for bridge in bridges[one]:
    islands.append(bridge[:])
my_max = 0
bfs()
print(my_max)
'''