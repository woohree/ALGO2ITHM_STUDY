from itertools import combinations
import sys
sys.stdin = open('M.txt')

INF = float('inf')


def get_chicken_dist():
    combs = list(combinations(stores, M))       # M개의 치킨집 좌표 조합
    min_total = INF                             # 모든 집의 최소 치킨거리의 합

    for comb in combs:
        temp_total = 0                          # 조합 별 최소 치킨거리의 합
        for house in houses:                    # 집 별 최소 치킨거리 계산
            temp_min_dist = INF
            for r, c in comb:
                temp_dist = abs(house[0] - r) + abs(house[1] - c)
                if temp_min_dist > temp_dist:
                    temp_min_dist = temp_dist
            temp_total += temp_min_dist
        if min_total > temp_total:
            min_total = temp_total

    return min_total


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

houses, stores = [], []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:       # 집일 떄
            houses.append((i, j))
        elif matrix[i][j] == 2:     # 치킨집일 때
            stores.append((i, j))

print(get_chicken_dist())
