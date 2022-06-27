import sys, heapq
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
lectures = []
for _ in range(N):
    num, s, e = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(lectures, (s, e))

classroom = []
for _ in range(N):
    s, e = heapq.heappop(lectures)
    if classroom and classroom[0] <= s:
        heapq.heappop(classroom)
    heapq.heappush(classroom, e)
print(len(classroom))
