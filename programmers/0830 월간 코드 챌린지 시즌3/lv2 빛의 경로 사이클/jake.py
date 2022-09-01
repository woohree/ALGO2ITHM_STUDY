direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]
left = [3, 0, 1, 2]
right = [1, 2, 3, 0]


def solution(grid):
    answer = []
    # 격자의 너비와 높이를 생성
    width, height = len(grid[0]), len(grid)
    # 한 번이라도 통과한 건 의미가 없으므로 한꺼번에 모든 check를 만들어줌(visited)
    check = [[[False] * 4 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            for i in range(4):
                # 이미 이동한 적 있는 방향은 판단 X
                if check[y][x][i]:
                    continue
                # 사이클의 길이
                cnt = 0
                now_y, now_x, now_dir = y, x, i
                # while문을 진행하면서 사이클이 생성되는지 확인함
                while True:
                    check[now_y][now_x][now_dir] = True
                    cnt += 1
                    grid_name = grid[now_y][now_x]
                    # 현재 격자의 값을 확인하여 방향 결정
                    if grid_name == 'L':
                        now_dir = left[now_dir]
                    elif grid_name == 'R':
                        now_dir = right[now_dir]
                    now_x, now_y = (now_x + direction[now_dir][0]) % width, (now_y + direction[now_dir][1]) % height
                    # 처음 출발점에 도착하면 완료
                    if now_x == x and now_y == y and now_dir == i:
                        break
                answer.append(cnt)

    # 값을 정렬 후 리턴
    answer.sort()
    return answer

# 제일 힘들었던 건 right, left 방향 확인하는 것
# + width와 height로 나머지 구하는 것