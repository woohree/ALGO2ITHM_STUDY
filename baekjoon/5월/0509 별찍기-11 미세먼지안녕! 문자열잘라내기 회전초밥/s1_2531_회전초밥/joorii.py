from collections import deque
import sys
sys.stdin = open('M.txt')

# 접시의 수 N, 가짓수 d, 연속해서 먹는 접시 수 k, 쿠폰 번호 c
N, d, k, c = map(int, sys.stdin.readline().split())
dishes = []
for _ in range(N):
    dishes.append(int(sys.stdin.readline()))
ans = 0
dq = deque(dishes[0:k])
for i in range(N):
    dq.append(c)                # 쿠폰 접시 추가
    if len(set(dq)) >= ans:
        ans = len(set(dq))
    dq.popleft()
    dq.pop()
    nxt = k + i if k + i < N else k + i - N
    dq.append(dishes[nxt])

print(ans)

