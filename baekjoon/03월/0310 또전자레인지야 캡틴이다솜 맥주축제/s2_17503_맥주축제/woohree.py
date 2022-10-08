import sys
sys.stdin = open('L.txt')
# 1930 start

from collections import deque


def liver_level_for_festival():
    pass


N, M, K = map(int, sys.stdin.readline().rstrip().split())
beers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(K)]
# my_sort(beers)
beers.sort()
# print(beers)
ans = liver_level_for_festival()
print(ans)

# def my_sort(a):
#     b = len(a)
#     for i in range(b-1, 0, -1):
#         for j in range(i):
#             if a[j][1] > a[j+1][1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# def liver_level_for_festival():
#     result = deque()
#     preference = 0
#     levels = deque()
#     for i in range(N):
#         a = beers.pop()
#         result.append(a)
#         preference += a[0]
#         levels.append(a[1])
#
#     for j in range(K-N):
#         a = beers.pop()
#         for k in range(N):
#             if a[1] < result[k][1] and preference+a[0]-result[k][0] >= M:
#                 # b = result.popleft()
#                 result.append(a)
#                 preference += a[0]
#                 preference -= result[k][0]
#                 levels.remove(result[k][1])
#                 levels.append(a[1])
#                 result.remove(result[k])
#                 break
#
#     max_level = max(levels)
#     if not beers and preference < M:
#         return -1
#
#     return max_level