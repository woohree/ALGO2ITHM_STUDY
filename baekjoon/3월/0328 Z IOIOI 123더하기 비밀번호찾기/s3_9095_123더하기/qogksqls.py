import sys
sys.stdin = open('B.txt')

# 1. 순열썼다 메모리초과
# 2. dp

# dp
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    #     1, 2, 3
    dp = [1, 2, 4]
    if n == 1:
        print(dp[0])
    elif n == 2:
        print(dp[1])
    elif n == 3:
        print(dp[2])
    else:
        while n != 3:
            temp = sum(dp)
            dp[0], dp[1], dp[2] = dp[1], dp[2], temp
            n -= 1
        print(dp[2])

# 순열 풀이
# import itertools
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     numbers = [0] * (n//3 + n%3) + [1] * n + [2] * (n//2) + [3] * (n//3)
#     perm = list(itertools.permutations(numbers, n))
#
#     result = []
#     for p in perm:
#         if sum(p) == 4:
#             result.append(p)
#     result = list(set(result))
#
#     temp_result = []
#     for r in result:
#         temp = []
#         for i in range(4):
#             if r[i] == 1:
#                 temp.append(1)
#             elif r[i] == 2:
#                 temp.append(2)
#             elif r[i] == 3:
#                 temp.append(3)
#         temp_result.append(temp)
#
#     answer = []
#     for t in temp_result:
#         if t not in answer:
#             answer.append(t)
#
#     print(len(answer))
