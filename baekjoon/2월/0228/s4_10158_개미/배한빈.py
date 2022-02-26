# 130분
# 좌표 이동하는 방식으로 짜기
# 모서리에 닿았을 떄 생각하기

# 모든 경우 if문으로 조건 달아서 설정 => 시간초과
# 점화식으로 구현

import sys
sys.stdin = open('B.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
hour = int(input())

# while문 돌려서 경우의 수 조건 설정한 다음에 하나씩 돌리는 느낌
# 시간초과로 pass 못한다.

# x, y 이동값
dx = [1, -1]
dy = [1, -1]

# m, n은 dx와 dy의 인덱스, 그냥 0과 1로만 바뀔 예정
# 초기값은 dx와 dy가 1로 되도록 m,n은 0으로 설정
m = n = 0
time = 1
current = [p, q]  # 현재 위치

while time <= hour:
    current[0] += dx[m]
    current[1] += dy[n]

    # 벽에 부딪힐 경우
    if current[0] == w or current[0] == 0 or current[1] == h or current[1] == 0:
        # x값이 w 벽에 부딪혔을 때
        if current[0] == w:
            # 오른쪽 상단 모서리 만났을 경우, dx와 dy는 -1 값으로 바꿔줘야 한다.
            if current[1] == h:
                m = n = 1
            # 오른쪽 하단 모서리 만났을 경우, dx는 -1 dy는 1로 바꿔줘야 한다.
            elif current[1] == 0:
                m, n = 1, 0
            # 그외 그냥 w인 벽에 부딪혔을 경우, m만 바꿔준다.
            else:
                m = (m + 1) % 2

        # x값이 0 벽에 부딪혔을 때, 위와 비슷하다.
        elif current[0] == 0:
            if current[1] == h:
                m, n = 0, 1
            elif current[1] == 0:
                m = n = 0
            else:
                m = (m + 1) % 2

        # 그 외, y값만 벽에 부딪혔을 경우
        elif current[1] == h or current[1] == 0:
            n = (n + 1) % 2

    time += 1

print(*current)

# ----------------------------------------------------------
# 점화식 생각하다가 구현
# x와 y가 각각 벽을 몇번 터치하는지 구한다.
p_touch_wall = (p + hour) // w
q_touch_wall = (q + hour) // h

# 그리고 나머지를 구한다.
p_move = (p + hour) % w
q_move = (q + hour) % h

# 위치는 처음에 오린쪽 위로 이동하므로 각각 벽을 한번 만났을 때는 좌표 위치가 뒤로 간다.
# 따라서 벽을 터피한 횟수가 홀수일 때는 전체 길이에서 나머지 구한걸 뺴주고
# 짝수일 때는 그 값이 그대로 좌표 위치
if p_touch_wall % 2:
    p = w - p_move
else:
    p = p_move

if q_touch_wall % 2:
    q = h - q_move
else:
    q = q_move

print(p, q)
