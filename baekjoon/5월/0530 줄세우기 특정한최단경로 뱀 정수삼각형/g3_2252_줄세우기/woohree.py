import sys
from collections import deque
sys.stdin = open('L.txt')


def topological_sort(lst):          # 위상 정렬
    sorted_lst = []
    q = deque()

    for i in range(1, N+1):         # 진입 차수가 0인 원소만 큐에 추가
        if not indegree[i]:
            q.append(i)

    while q:                        # 큐가 True인 동안,
        now = q.popleft()           # 원소 하나씩 빼면서
        sorted_lst.append(now)
        for i in lst[now]:          # 현재 선택한 원소(now)에서 진출하는 원소들의 진입 차수 -1
            indegree[i] -= 1
            if not indegree[i]:     # 새롭게 진입 차수가 0이 된 원소들, 큐에 삽입
                q.append(i)

    return sorted_lst


N, M = map(int, sys.stdin.readline().rstrip().split())
indegree = [0] * (N+1)              # 각 학생 별 진입 차수 저장
students = [[] for _ in range(N+1)] # 각 학생 별 연결된 학생
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    students[a].append(b)           # a와 연결된 b
    indegree[b] += 1                # => b의 진입차수 +1
ans = topological_sort(students)
for i in ans:
    print(i, end=' ')