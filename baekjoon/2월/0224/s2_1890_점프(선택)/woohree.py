import sys
sys.stdin = open('L.txt')
sys.setrecursionlimit(10**8)
# 2100 start
# 2230 Restart

# DFS로 풀다가 시간초과 자꾸 나서 포기함..
# 총 120분 ㅋㅋ 아

# 맵 쭉 돌면서 각 위치에 도달하는 총 경우의 수를 각각 다 구함
def jump_to_goal(game_map, N):
    # (0, 0) 경우의 수 1에서 출발
    cnt_map[0][0] = 1
    for row in range(N):
        for col in range(N):
            # 마지막 칸에서 부시고 나와야 함
            # 아니면 값이 0이라 지 혼자서 또 더함
            if row == N-1 and col == N-1:
                break
            # cnt_map은 경우의 수 세는 지도,
            # game_map은 입력받은 지도
            location = game_map[row][col]
            # 아래, 오른쪽 움직임
            new_row, new_col = row + location, col + location
            if new_row < N:
                cnt_map[new_row][col] += cnt_map[row][col]
            if new_col < N:
                cnt_map[row][new_col] += cnt_map[row][col]


N = int(input())
game_map = [list(map(int, input().split())) for _ in range(N)]
cnt_map = [[0]*N for _ in range(N)]
jump_to_goal(game_map, N)
print(cnt_map[N-1][N-1])

# DFS ㅜ^ㅜ

# def jump_to_goal(location, row, col):
#     global cnt
#     if row == N-1 and col == N-1:
#         cnt += 1
#         return
#     elif location == 0:
#         return
#
#     moves = [[1, 0], [0, 1]]
#
#     for move in moves:
#         new_row, new_col = row + (move[0] * location), col + (move[1] * location)
#         if new_row < N and new_col < N:
#             if not visited[new_row][new_col]:
#                 new_location = game_map[new_row][new_col]
#                 jump_to_goal(new_location, new_row, new_col)
#
# N = int(input())
# game_map = [list(map(int, input().split())) for _ in range(N)]
# start = game_map[0][0]
# visited = [[False]*N for _ in range(N)]
# cnt = 0
# jump_to_goal(start, 0, 0)
# print(cnt)
