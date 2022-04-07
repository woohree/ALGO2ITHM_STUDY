from collections import deque
import sys
sys.stdin = open('G.txt')

def solution(relations):
    global n, want_x, want_y

    # 방문했는지 안 했는지 확인하기 위한 배열
    visited = [0] * (n+1)

    queue = deque()
    # 현재 위치 추가
    queue.append(want_x)
    while queue:
        k = queue.popleft()
        # k사람과 관계가 있는 사람들을 반복
        for j in relations[k]:
            # j번 사람을 방문하지않았다면
            if not visited[j]:
                # k번 사람의 관계에 + 1
                visited[j] = visited[k] + 1
                queue.append(j)

    if visited[want_y] == 0:
        return -1
    else:
        return visited[want_y]


n = int(input())
want_x, want_y = map(int, input().split())
relation_cnt = int(input())
relations = [[] for _ in range(n+1)]

for i in range(relation_cnt):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)

answer = solution(relations)
print(answer)