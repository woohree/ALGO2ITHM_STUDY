from collections import deque
import heapq
import sys
sys.stdin = open('M.txt')

N = int(sys.stdin.readline())
lectures, rooms = [], []
for _ in range(N):
    i, s, e = map(int, sys.stdin.readline().split())
    lectures.append((s, e))
lectures.sort(key=lambda x: x[0])   # 시작시간 기준 오름차순 정렬

answer = 0
for lecture in lectures:
    s, e = lecture
    while rooms and s >= rooms[0][0]:   # 다음 강의의 시작시간이 진행 중인 가장 일찍 끝나는 강의의 종료시간과 같거나 늦을 때
        heapq.heappop(rooms)
    heapq.heappush(rooms, (e, s))   # 종료시간 기준 오름차순 정렬
    if len(rooms) > answer:
        answer = len(rooms)

print(answer)
