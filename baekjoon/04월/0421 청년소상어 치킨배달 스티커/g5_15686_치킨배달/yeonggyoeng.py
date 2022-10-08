import sys, heapq
from itertools import combinations
sys.stdin = open('G.txt')

# N * N , M개
N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 0 -> 빈 칸, 1 -> 집, 2 -> 치킨
home = []
chicken = []
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1:
            home.append((row, col))
        elif matrix[row][col] == 2:
            chicken.append((row, col))

# 치킨집에서 집까지의 거리
chicken_to_home = []

for ch in chicken:
    # 집에서 치킨집 까지의 거리
    home_to_chicken = []
    for h in home:
        dist = abs(ch[0] - h[0]) + abs(ch[1] - h[1])
        home_to_chicken.append(dist)
    
    chicken_to_home.append(home_to_chicken)

answer = N ** N
for comb in combinations(range(len(chicken)), M):
    min_dist = 0
    for house in range(len(home)):
        min_dist += min([chicken_to_home[i][house] for i in comb])

    if min_dist < answer:
        answer = min_dist
print(answer)


# '''
# heap에다가 넣기
# [치킨거리, 집번호, 치킨집 번호]
# 집이 다 나오고 치킨집의 개수가 M개면 스탑
# '''
# distances = []
# for i, chicken in enumerate(chickens):
#     for j, home in enumerate(homes):
#         distance = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
#         heapq.heappush(distances, [distance, i, j])
#
# min_distance = 0
# store = []
# while distances:
#
#     dist, chicken, home = heapq.heappop(distances)
#     if type(homes[home]) == tuple:
#         min_distance += dist
#         homes[home] = 0
#         if chicken not in store:
#             store.append(chicken)
#     if homes == [0] * len(homes):
#         break
#     if len(store) == M and homes == [0] * len(homes):
#         break
# print(chickens)
# print(store)
# print(min_distance)