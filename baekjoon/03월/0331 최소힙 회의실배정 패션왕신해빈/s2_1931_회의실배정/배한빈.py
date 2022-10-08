# 화물 도크랑 엄청 비슷한데?
# 근데 안되네?
# 1. 화물 도크랑 비슷하게 풀었다. 재귀 돌렸음. 5% 시간초과
# 2. list가 문제인가 싶어 dict로 바꿔서 풀었음. 5% 시간초과
# 3. 질문 좀 검색하다가 원래 sort랑 list 때문에 시간초과 난 줄 알았는데 사람들 다 list랑 sort 쓰길래 다시 돌아옴. slice 빼서 품. 5% 시간초과
# 4. 그냥 처음부터 문제를 잘못 이해했다.
# 5% 시간초과 이유는 이중 for 문을 사용해서다. 이중포문 사용하면 시간복잡도가 O(n**2)이 나온단다.
# 근데 이중포문 안쓰고 검사를 어떻게 하나 싶었는데 그냥 정렬을 1. 끝나는 시간 2. 시작 시간 순으로 정렬하고 for 문 한번만 쓰니까 풀린다...
# 우현님이 수업시간에 설명한게 이거구나 싶었다.
# 너무 억울하다. 내 두 시간...

import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
times = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))

time = 1
temp = times[0]
for i in range(1, N):
    if temp[1] <= times[i][0]:
        time += 1
        temp = times[i]

print(time)


# def solution(start):
#     global time, my_max
#
#     if my_max < time:
#         my_max = time
#
#     for t in range(start+1, len(trucks)):
#         if temp[-1][1] <= trucks[t][0]:
#             temp.append(trucks[t])
#             time += 1
#             solution(t)
#             time -= 1
#             temp.pop()
#     return


# def solution(end_time):
#     global time, my_max
#
#     if my_max < time:
#         my_max = time
#
#     for i in range(max(meetings)+1 - end_time):
#         if end_time + i in meetings:
#             time += 1
#             a = meetings[end_time + i]
#             for b in a:
#                 solution(b)
#             time -= 1
#     return
#

# N = int(sys.stdin.readline().rstrip())
#
# meetings = {}
# for n in range(N):
#     start, end = map(int, sys.stdin.readline().rstrip().split())
#     if start not in meetings:
#         meetings[start] = [end]
#     else:
#         meetings[start].append(end)
#
# my_max = 1
# for meeting in meetings:
#     ends = meetings[meeting]
#     for e in ends:
#         time = 1
#         solution(e)
#
# print(my_max)
