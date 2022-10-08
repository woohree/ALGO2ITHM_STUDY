# 1명의 경비원
# N x N 2차원 지도
# 통로는 0, 벽은 1, 경비원은 2
# 상하좌우로만 감시, 감시 거리는 무한
# 감시할 수 없는 영역을 사각지대
# 사각지대의 개수를 출력, 없을 경우 0 출력
import sys
sys.stdin = open('input.txt')


def get_location_and_zero():
    global zero_count
    for i in range(N):
        for j in range(N):
            if jido[i][j] == 2:
                security_location.append(i)
                security_location.append(j)
            elif jido[i][j] == 0:
                zero_count += 1
    return security_location, zero_count


def check_possible_zero():
    global check
    for m in range(4):
        temp_location = [security_location[0], security_location[1]]
        for n in range(N):
            if 0 <= temp_location[0] + move[m][0] < N and 0 <= temp_location[1] + move[m][1] < N and jido[temp_location[0] + move[m][0]][temp_location[1] + move[m][1]] != 1:
                temp_location[0] += move[m][0]
                temp_location[1] += move[m][1]
                check += 1
            else:
                break
    return check


# 상,하,좌,우 이동할 수 있는 변수
# 값이 2인 곳에서 위로 가다가 범위 벗어나거나 1 만나면 stop
# 이동할 때마다 count
# stop하면 다시 제자리로 돌아와서 검사
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]

    # 이동시키기
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 경비 현재 위치 찾기, 벽 아닌곳 개수 구하기
    security_location = []
    zero_count = 0
    get_location_and_zero()

    # check 가능한 통로 개수 count
    check = 0
    check_possible_zero()

    print(f'#{tc} {zero_count - check}')
