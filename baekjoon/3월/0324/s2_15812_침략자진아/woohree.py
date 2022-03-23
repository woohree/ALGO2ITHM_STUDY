import sys, itertools, copy
from collections import deque
sys.stdin = open('L.txt')


def ffind(m):                               # 빈 공간과 마을 위치 찾는 함수
    blank = []
    town = []
    for i in range(N):
        for j in range(M):
            if not m[i][j]:
                blank.append((i, j))
            else:
                town.append((i, j))
    return blank, town


# 행성을 초토화시키려면,
# 독 주머니에서 ((가장 먼 마을))까지 가는 거리만큼 시간이 걸린다.
# 독 주머니가 2개기 때문에, 1에서 더 먼 마을은 2가 먼저 초토화시킨다.
# 따라서,
# 1. 독 주머니 2개와 마을의 거리를 각각 구하고,
# 2. ((거리가 가까운 독 주머니와 마을의 거리))와 총 걸리는 시간을 비교하면서,
# 3. 가장 먼 마을까지 초토화시키는 시간을 구한다.
def kill_planet(r1, c1, r2, c2):
    time = 0
    for town in towns:
        distance_poison1 = abs(town[0]-r1) + abs(town[1]-c1)
        distance_poison2 = abs(town[0]-r2) + abs(town[1]-c2)
        if distance_poison1 > distance_poison2:
            if distance_poison2 > time:
                time = distance_poison2
        else:
            if distance_poison1 > time:
                time = distance_poison1
    return time


N, M = map(int, sys.stdin.readline().rstrip().split())
m = [list((map(int, sys.stdin.readline().rstrip()))) for _ in range(N)]
blanks, towns = ffind(m)
comb = list(itertools.combinations(blanks, 2))
ans = N*M
for idx in range(len(comb)):
    T = kill_planet(comb[idx][0][0], comb[idx][0][1], comb[idx][1][0], comb[idx][1][1])
    if T < ans:
        ans = T
print(ans)



# BFS방식

# def kill_planet(r1, c1, r2, c2):
#     t = 0
#     copy_m[r1][c1] = 2
#     copy_m[r2][c2] = 2
#     moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     news1 = deque()
#     news2 = deque()
#     news1.append((r1, c1))
#     news2.append((r2, c2))
#
#     while news1 or news2:
#         t += 1
#         for _ in range(len(news1)):
#             new1 = news1.popleft()
#             for move in moves:
#                 new_r1, new_c1 = new1[0] + move[0], new1[1] + move[1]
#                 if 0 <= new_r1 < N and 0 <= new_c1 < M and copy_m[new_r1][new_c1] != 2:
#                     copy_m[new_r1][new_c1] = 2
#                     news1.append((new_r1, new_c1))
#         for _ in range(len(news2)):
#             new2 = news2.popleft()
#             for move in moves:
#                 new_r2, new_c2 = new2[0] + move[0], new2[1] + move[1]
#                 if 0 <= new_r2 < N and 0 <= new_c2 < M and copy_m[new_r2][new_c2] != 2:
#                     copy_m[new_r2][new_c2] = 2
#                     news2.append((new_r2, new_c2))
#
#         trigger = 0
#         for town in m_data[1]:
#             if copy_m[town[0]][town[1]] == 1:
#                 trigger = 1
#                 break
#         if not trigger:
#             break
#     return t

# N, M = map(int, sys.stdin.readline().rstrip().split())
# m = [list((map(int, sys.stdin.readline().rstrip()))) for _ in range(N)]
# m_data = ffind(m)
# comb = list(itertools.combinations(m_data[0], 2))
# ans = N * M
# for idx in range(len(comb)):
#     copy_m = copy.deepcopy(m)
#     T = kill_planet(comb[idx][0][0], comb[idx][0][1], comb[idx][1][0], comb[idx][1][1])
#     if T < ans:
#         ans = T
# print(ans)