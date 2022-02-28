import sys
sys.stdin = open('G.txt')

def get_position():
    # 입력 받기
    w, h = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())

    # x, y 분리하여 해결
    # x_moves [ 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1] -> x가 다닐수 있는 범위
    # y_moves [ 0, 1, 2, 3, 4, 3, 2, 1] -> y가 다닐 수 있는 범위
    x_moves_go = [i for i in range(w)]
    x_moves_back = [i for i in range(w, 0, -1)]
    x_moves = x_moves_go + x_moves_back
    y_moves_go = [i for i in range(h)]
    y_moves_back = [i for i in range(h, 0, -1)]
    y_moves = y_moves_go + y_moves_back

    # index -> 현재 좌표 + 시간을 다닐 수 있는 범위의 길이로 나눈 몫
    new_x = x_moves[(x+t) % (2*w)]
    new_y = y_moves[(y+t) % (2*h)]
    return new_x, new_y

answer = get_position()
answer = ' '.join(map(str, answer))
print(answer)