import sys
sys.stdin = open('input2.txt')


# 컴퓨테이셔널 띵킹을 했더니,
# 휴먼 띵킹을 강요하네
def get_location_after_hours(w, h, p, q, t):
    # 그냥 간단하게 대각선말고
    # 가로, 세로로 어떻게 움직이는지 생각해야 함
    # 시간만큼 가로, 세로로 증가하다가 감소를 반복
    temp_p, temp_q = p+t, q+t
    if w <= temp_p % (2*w) < 2*w:  # 시간만큼 가로로 어떻게 움직였는지
        new_p = w - (temp_p % w)
    else:
        new_p = temp_p % w

    if h <= temp_q % (2*h) < 2*h:  # 시간만큼 세로로 어떻게 움직였는지
        new_q = h - (temp_q % h)
    else:
        new_q = temp_q % h

    return new_p, new_q


w, h = map(int, input().split())
# p, q1 = map(int, input().split())
# q = h - q1
# matrix = [[0]*(w+1) for _ in range(h+1)]
p, q = map(int, input().split())
t = int(input())
ans = get_location_after_hours(w, h, p, q, t)
print(ans[0], ans[1])


# 컴퓨테이셔널 띵킹의 흔적들..
# 억울하다!

# while문으로 품
# def get_location_after_hours(q, p):
#     moves = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
#     time = 0
#     direction = 0
#
#     while time < t:
#         time += 1
#         if (p == 0 or p == w) and (q == 0 or q == h):
#             direction = (direction+2) % 4
#
#         elif q == 0 or q == h or p == 0 or p == w:
#             if p == w or p == 0:
#                 if direction == 0 or direction == 2:
#                     direction += 1
#                 else:
#                     direction -= 1
#
#             elif q == h or q == 0:
#                 if direction == 0 or direction == 2:
#                     direction = (direction+3) % 4
#                 else:
#                     direction += 1
#
#         new_q, new_p = q + moves[direction][0], p + moves[direction][1]
#         q, p = new_q, new_p
#
#     return p, h-q

# 재귀로 품
# def get_location_after_hour(p, q, direction):
#     global time, moves, w, h
#     if time == t:
#         print(p, h-q)
#         return
#
#     time += 1
#     if (p == 0 or p == w) and (q == 0 or q == h):
#         new_direction = direction + 2
#         if new_direction > 3:
#             new_direction %= 4
#
#     elif q == 0 or q == h or p == 0 or p == w:
#         if p == w:
#             if direction == 0:
#                 new_direction = 1
#             else:
#                 new_direction = 2
#         elif p == 0:
#             if direction == 1:
#                 new_direction = 0
#             else:
#                 new_direction = 3
#         elif q == h:
#             if direction == 3:
#                 new_direction = 0
#             else:
#                 new_direction = 1
#         elif q == 0:
#             if direction == 0:
#                 new_direction = 3
#             else:
#                 new_direction = 2
#     else:
#         new_direction = direction
#
#     new_q, new_p = q + moves[new_direction][0], p + moves[new_direction][1]
#     get_location_after_hour(new_p, new_q, new_direction)