# baekjoon 1012 유기농배추

# 테스트 케이스 T 
# 배추밭 가로길이 M / 배추밭 세로길이 N / 배추 위치 개수 K
# 배추의 위치 X, Y 

# 1. 배추밭 리스트를 반복문을 통해 전체 탐색하면서 
# 2. 배추밭 리스트에 배추가 있을 때 (cabbage_list == 1)
# 3. 체크용 리스트에서 해당 위치 상하좌우에 또 다른 배추가 있는지 조사
# 3 - 1. 체크용 리스트에서 해당 위치 상하좌우에 다른 배추가 없다면, 0 -> 1 변환 후 count 1 증가
# 3 - 2. 체크용 리스트에서 해당 위치 상하좌우에 다른 배추가 있다면, 0 -> 1 변환

t = int(input())

for tc in range(t):
    m, n, k = map(int, input().split())

    # 배추밭 리스트
    cabbage_list = [[0] * m for _ in range(n)]
    check_list = [[0] * m for _ in range(n)] 
    move_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    count = 0

    for _ in range (k):
        x, y = map(int, input().split())
        cabbage_list[y][x] = 1

    for i in range(len(check_list)):
        for j in range(len(check_list[i])):

            if cabbage_list[i][j] == 1:
                for move in move_list:
                    # 배추밭 범위를 벗어났을 때 
                    # out of range
                    if (i + move[0] < 0) or (j + move[1] < 0) or (i + move[0] >= n) or (j + move[1] >= m):
                        continue
                    # 주변에 다른 배추흰지렁이 영역이 있을 때
                    elif check_list[i + move[0]][j + move[1]] == 1:
                        check_list[i][j] = 1
                        break
                
                # 주변에 다른 배추흰지렁이가 없을 때
                if check_list[i][j] == 0:
                    count += 1
                    check_list[i][j] = 1

    print(f'{count}')
