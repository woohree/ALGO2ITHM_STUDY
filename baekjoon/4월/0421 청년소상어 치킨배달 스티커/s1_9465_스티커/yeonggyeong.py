import heapq
import sys
sys.stdin = open('G.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(2)]

    '''
    50 10 100 20 40
    30 50 70  10 60 
    '''
    '''
    50 40 200 140 250
    30 100 120 210 260
    '''
    
    dp = [[0 for _ in range(N)] for _ in range(2)]

    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]

    for col in range(1, N):
        if col == 1:
            dp[0][col] = dp[1][col-1] + matrix[0][col]
            dp[1][col] = dp[0][col-1] + matrix[1][col]
        else:
            dp[0][col] = max(dp[1][col-2], dp[1][col-1]) + matrix[0][col]
            dp[1][col] = max(dp[0][col-2], dp[0][col-1]) + matrix[1][col]

    print(max(dp[0][N-1], dp[1][N-1]))

# def solution():
#     max_score = 0
#     while True:

#         if not heap:
#             return max_score

#         sticker = heapq.heappop(heap)
#         while matrix[sticker[1][0][0]][sticker[1][0][1]] < 0:
#             if heap:
#                 sticker = heapq.heappop(heap)
#             else:
#                 return max_score

#         max_score += sticker[0]
#         for i, j in sticker[1]:
#             matrix[i][j] = -1


# T = int(sys.stdin.readline())

# for tc in range(T):
#     N = int(sys.stdin.readline())
#     matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
#     heap = []

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     for row in range(2):
#         for col in range(N):

#             share = [(row, col)]
#             for idx in range(4):
#                 new_row, new_col = row + dx[idx], col + dy[idx]
#                 if 0 <= new_row < 2 and 0 <= new_col < N:
#                     share.append((new_row, new_col))
#             heapq.heappush(heap, [-matrix[row][col], share])
#     answer = solution()

#     print(-answer)