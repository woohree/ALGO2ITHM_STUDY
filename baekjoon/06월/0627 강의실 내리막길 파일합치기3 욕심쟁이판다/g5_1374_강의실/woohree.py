import sys, heapq
sys.stdin = open('L.txt')


N = int(input())
starts = []                                     # 시작시간 기준 최소힙
ends = []                                       # 종료시간 기준 최소힙
for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().rstrip().split())
    starts.append((s, e))
heapq.heapify(starts)
heapq.heappush(ends, heapq.heappop(starts)[1])  # 첫 비교군 만들기

cnt = 1
while starts:
    s, e = heapq.heappop(starts)
    if s >= ends[0]:                            # 시작 시각이 가장 빨리 끝나는 시각보다 늦으면,
        heapq.heappop(ends)                     # 강의실 같은거 사용!
    else:
        cnt += 1                                # 그외, 다른 강의실 +1
    heapq.heappush(ends, e)                     # 끝나는 시각 추가
print(cnt)

# N = int(input())
# times = []
# for _ in range(N):
#     n, s, e = map(int, sys.stdin.readline().rstrip().split())
#     times.append([e, s, n])
# heapq.heapify(times)
#
# e, s, n = heapq.heappop(times)
# temps = [e]
# cnt = 1
# for i in range(1, N):
#     e, s, n = heapq.heappop(times)
#     for j in range(len(temps)):
#         if s >= temps[j]:
#             temps[j] = e
#             break
#     else:
#         cnt += 1
#         temps.append(e)
# print(cnt)


# N = int(input())
# times = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# times.sort(key=lambda x: (x[2]))
# temp = times[0][2]
# temps = [[temp]]
# cnt = 1
# for i in range(1, N):
#     for j in range(len(temps)):
#         if times[i][1] >= temps[j][-1]:
#             temps[j].append(times[i][2])
#             break
#     else:
#         cnt += 1
#         temps.append([times[i][2]])
# print(cnt)