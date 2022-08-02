import sys
sys.stdin = open('input.txt')

def Foward(roboto, direction, times):

    if times == 0:
        return

    # 동쪽을 바라볼 때
    if direction == 'E':
        # y축을 하나씩 더하면서 이동
        if robot[roboto][0]+1 > A:
            return error.append(f'Robot {roboto} crashes into the wall')
        elif [robot[roboto][0]+1, robot[roboto][1]] in robot:
            for i in range(N+1):
                if robot[i] == [robot[roboto][0]+1, robot[roboto][1]]:
                    return error.append(f'Robot {roboto} crashes into robot {i}')
        else:
            robot[roboto][0] += 1
            Foward(roboto, direction, times-1)

    # 서쪽을 바라볼 때
    elif direction == 'W':
        # y축을 하나씩 빼면서 이동
        if robot[roboto][0] - 1 < 1:
            return error.append(f'Robot {roboto} crashes into the wall')
        elif [robot[roboto][0]-1, robot[roboto][1]] in robot:
            for i in range(N+1):
                if robot[i] == [robot[roboto][0]-1, robot[roboto][1]]:
                    return error.append(f'Robot {roboto} crashes into robot {i}')
        else:
            robot[roboto][0] -= 1
            Foward(roboto, direction, times - 1)
    # 남쪽을 바라볼 때
    elif direction == 'S':
        # x축을 하나씩 빼면서 이동
        if robot[roboto][1] - 1 < 1:
            return error.append(f'Robot {roboto} crashes into the wall')
        elif [robot[roboto][0], robot[roboto][1]-1] in robot:
            for i in range(N+1):
                if robot[i] == [robot[roboto][0], robot[roboto][1]-1]:
                    return error.append(f'Robot {roboto} crashes into robot {i}')
        else:
            robot[roboto][1] -= 1
            Foward(roboto, direction, times - 1)
    # 북쪽을 바라볼 때
    elif direction == 'N':
        # x축을 하나씩 더하면서 이동
        if robot[roboto][1] + 1 > B:
            return error.append(f'Robot {roboto} crashes into the wall')
        elif [robot[roboto][0], robot[roboto][1]+1] in robot:
            for i in range(N+1):
                if robot[i] == [robot[roboto][0], robot[roboto][1] + 1]:
                    return error.append(f'Robot {roboto} crashes into robot {i}')
        else:
            robot[roboto][1] += 1
            Foward(roboto, direction, times - 1)
    if error:
        return

def Turn(num, direction, times, turn_dir):
    if times == 0:
        return
    if direction[num] == 'E':

        # 동쪽 보면 북쪽으로 좌회전
        if turn_dir == 'L':
            direction[num] = 'N'

        # 동쪽 보면 남쪽으로 우회전
        else:
            direction[num] = 'S'

    elif direction[num] == 'W':
        # 서쪽 보면 남쪽으로 좌회전
        if turn_dir == 'L':
            direction[num] = 'S'
        # 서쪽 보면 북쪽으로 우회전
        else:
            direction[num] = 'N'

    elif direction[num] == 'S':
        # 남쪽 보면 동쪽으로 좌회전
        if turn_dir == 'L':
            direction[num] = 'E'
        # 남쪽 보면 서쪽으로 우회전
        else:
            direction[num] = 'W'

    elif direction[num] == 'N':
        # 북쪽 보면 서쪽으로 좌회전
        if turn_dir == 'L':
            direction[num] = 'W'
        # 북쪽 보면 동쪽으로 우회전
        else:
            direction[num] = 'E'
    Turn(num, direction, times - 1, turn_dir)

# 땅의 크기(y축, x축인 것에 주의
A, B = map(int, input().split())

# 로봇의 숫자, 명령의 숫자
N, M = map(int, input().split())

# 로봇 y, x축 저장해두는 장소
robot = []
# 1번부터 시작하므로 빈 배열 하나 추가
robot.append([])

# 로봇 보는 방향 저장해두는 장소
robot_directions = []

# 마찬가지로 1번부터 시작하므로 빈 방향 하나 추가
robot_directions.append('0')

# 에러 코드 담을 곳
error = []

for roboto in range(N):
    # y, x축을 따로 저장하고
    # 방향을 따로 저장
    y, x, direction = input().split()
    robot.append([int(y), int(x)])
    robot_directions.append(direction)
for order in range(M):
    order_robot, order_sort, times = input().split(
    # Foward 함수 이용해서 진행
    if order_sort == 'F':
        Foward(int(order_robot), robot_directions[int(order_robot)], int(times))
    # 왼쪽, 오른쪽 둘다 Turn 함수 이용해서 진행
    elif order_sort == 'L':
        Turn(int(order_robot), robot_directions, int(times), 'L')
    elif order_sort == 'R':
        Turn(int(order_robot), robot_directions, int(times), 'R')
    if error:
        print(*error)
        break
if not error:
    print("OK")