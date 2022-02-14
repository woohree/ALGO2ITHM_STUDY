# 80분

# 지도 그리기
def get_map(location, map):
    # R, L 등장 시,누적 횟수에 따른 이동 방향
    R = [[1,0], [0,-1], [-1,0], [0,1]]
    L = [[1,0], [0,1], [-1,0], [0,-1]]
    # F 등장 전까지, R, L의 등장 횟수 누적 
    jR = 0
    jL = 0
    # 시작지점 표시
    map[location[0]][location[1]] = '.'
    # 방향결정 + 이동
    for direction in directions:
        # R 등장 시,
        # R 등장 횟수 누적, 4 이상일 때 0으로 초기화
        if direction == 'R':
            jR += 1
            if jR == 4:
                jR = 0
        # L 등장 시,
        # L 등장 횟수 누적, 4 이상일 때 0으로 초기화
        elif direction == 'L':
            jL += 1
            if jL == 4:
                jL = 0
        # F 등장 시,
        elif direction == 'F':
            # R, L 등장 횟수가 같을 경우,
            # 남쪽으로 한 칸 이동
            if jR == jL:
                location[0] += 1
                map[location[0]][location[1]] = '.'
            # R, L 등장 횟수가 다른 경우,
            # R, L 등장 횟수 차이에 따라 이동
            elif jR > jL:
                location[0] += R[jR-jL][0]
                location[1] += R[jR-jL][1]
                map[location[0]][location[1]] = '.'
            elif jR < jL:
                location[0] += L[jL-jR][0]
                location[1] += L[jL-jR][1]
                map[location[0]][location[1]] = '.'
    return map

# 출력 가로 길이
def get_col(ans):
    col_list = []
    for row2 in range(len(ans)):
        for col in range(len(ans)):
            # '.' 이 나왔을 때, 인덱스를 뽑아 min, max 값을 출력 가로 길이로 씀
            if ans[row2][col] == '.':
                col_list.append(col)
    return [min(col_list), max(col_list)]

# 입력
length = int(input())
directions = input()
# 기본 지도 (한 변의 길이 101 인 정사각형)
map = [['#'] * 101 for _ in range(101)]
# 시작 위치, 지도의 중앙 지점
location = [50, 50]
# 출력
ans = get_map(location, map)
# print(ans)
for row in range(len(ans)):
    if not ans[row] == ['#'] * (101):
        a = get_col(ans)
        final_ans = ''.join(ans[row][a[0]:a[1]+1])
        print(final_ans)
