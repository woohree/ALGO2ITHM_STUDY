import sys, heapq
sys.stdin = open('G.txt')

N = int(sys.stdin.readline())

classes = [list(map(int, sys.stdin.readline().split()[1:])) for _ in range(N)]
# 시작 시간으로 정렬
classes.sort(key=lambda x: x[0])
# 첫번째 강의실 미리 준비
cnt = 1
finish_time = [classes[0][1]]

for cla in classes[1:]:
    # 가장 빨리 끝나는 강의 시간과 현재 강의의 시작 시간 비교
    # 강의가 끝난 후 현재 강의가 시작되는 경우
    if cla[0] >= finish_time[0]:
        heapq.heappop(finish_time)
    # 강의가 끝나지 않았을 때 현재 강의가 시작되는 경우
    else:
        cnt += 1
    heapq.heappush(finish_time, cla[1])
print(cnt)