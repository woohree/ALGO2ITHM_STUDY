import sys
sys.stdin = open('B.txt')

'''
K가 1, 2밖에 안 나오고 백준에 있는 출력값 보며 숫자 어디에 어떻게 들어가야 하는지 판단함

1. K가 1일 때, 원소를 1을 갖는 2x2 행렬 만들고 input 에 있는 x, y 좌표만 -1로 바꿈.
   단, 가장 왼쪽 아래가 (1, 1), 가장 오른쪽 위가 (2**K, 2**K)로 나온다.
2. K가 2일 경우 matrix를 아래와 같이 그냥 만들고 시작
3. 해당 좌표마다 그냥 일일이 다 계산
'''

K = int(sys.stdin.readline().rstrip())
x, y = map(int, sys.stdin.readline().rstrip().split())

if K == 1:
    matrix = [[1] * 2 for _ in range(2)]
    matrix[y%2][x-1] = -1
    for row in matrix:
        print(*row)

elif K == 2:
    matrix = [
        [4, 4, 5, 5],
        [4, 3, 3, 5],
        [1, 3, 3, 2],
        [1, 1, 2, 2]
    ]
    if y == 1:
        if x == 1:
            matrix[2][1] = 1
            matrix[y+2][x-1] = -1  # 1 1 -> 3 0
        elif x == 2:
            matrix[2][1] = 1
            matrix[y+2][x-1] = -1
        elif x == 3:
            matrix[2][2] = 2
            matrix[y+2][x-1] = -1
        else:
            matrix[2][2] = 2
            matrix[y+2][x-1] = -1  # 1 4 -> 3 3
    elif y == 2:
        if x == 1:
            matrix[2][1] = 1
            matrix[y][x-1] = -1  # 2 1 -> 2 0
        elif x == 2:
            matrix[y][x-1] = -1
        elif x == 3:
            matrix[y][x-1] = -1
        else:
            matrix[2][2] = 2
            matrix[y][x-1] = -1
    elif y == 3:
        if x == 1:
            matrix[1][1] = 4
            matrix[y-2][x-1] = -1  # 3 1 -> 1 0
        elif x == 2:
            matrix[y-2][x-1] = -1
        elif x == 3:
            matrix[y-2][x-1] = -1
        else:
            matrix[1][2] = 5
            matrix[y-2][x-1] = -1
    else:
        if x == 1:
            matrix[1][1] = 4
            matrix[y-4][x-1] = -1  # 4 1 -> 0 0
        elif x == 2:
            matrix[1][1] = 4
            matrix[y-4][x-1] = -1
        elif x == 3:
            matrix[1][2] = 5
            matrix[y-4][x-1] = -1
        else:
            matrix[1][2] = 5
            matrix[y-4][x-1] = -1  # 1 4 -> 3 3
    for row in matrix:
        print(*row)


