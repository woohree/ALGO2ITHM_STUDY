import sys, heapq
sys.stdin = open('G.txt')

N = int(input())

hw = [list(map(int, input().split())) for _ in range(N)]

# 마감기한으로 정렬
hw.sort()
# 가장 많이 남은 마감기한
date = hw[-1][0]
day = []
answer = 0

while True:
    # 종료조건
    if date == 0:
        break
    # 현재 date 에서 할 수 있는 과제들 day에 추가
    while hw and hw[-1][0] >= date:
        d, s = hw.pop()
        day.append((d, s))

    if day:
        # 현재 date에서 할 수 있는 과제 중 점수가 가장 높은 거 추가
        day.sort(key=lambda x: x[1])
        answer += day.pop()[1]

    date -= 1
print(answer)

# hw = []
# for _ in range(N):
#     deadline, score = map(int, input().split())
#     heapq.heappush(hw, (-deadline, -score))
#
# date = -hw[0][0]
#
# day = []
#
# answer = 0
# while True:
#     # 종료 조건
#     if date == 0:
#         break
#
#     d, s = heapq.heappop(hw)
#
#     while -d >= date:
#         heapq.heappush(day, (s, d))
#         if hw:
#             d, s = heapq.heappop(hw)
#         else:
#             break
#
#     heapq.heappush(hw, (d, s))
#
#     while day:
#         sc, da = heapq.heappop(day)
#         answer += -sc
#         break
#
#     while day:
#         s, d = heapq.heappop(day)
#         heapq.heappush(hw, (d, s))
#     date -= 1
# print(answer)