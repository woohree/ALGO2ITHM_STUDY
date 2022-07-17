import sys
from collections import deque
sys.stdin=open('input.txt')

one = list(input())
two = list(input())
three = list(input())
four = list(input())
for i in range(8):
    if one[i] == '1':
        one[i] = 1
    else:
        one[i] = 0
for i in range(8):
    if two[i] == '1':
        two[i] = 1
    else:
        two[i] = 0
for i in range(8):
    if three[i] == '1':
        three[i] = 1
    else:
        three[i] = 0
for i in range(8):
    if four[i] == '1':
        four[i] = 1
    else:
        four[i] = 0

one = deque(one)
two = deque(two)
three = deque(three)
four = deque(four)

K = int(input())
spin = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    # 체크박스를 미리 저장해 둠
    check_box = []
    if one[2] == two[6]:
        check_box.append(1)
    else:
        check_box.append(0)
    if two[2] == three[6]:
        check_box.append(1)
    else:
        check_box.append(0)
    if three[2] == four[6]:
        check_box.append(1)
    else:
        check_box.append(0)
    # 1번을 돌릴 때
    if spin[i][0] == 1:
        if spin[i][1] == 1:
            one.appendleft(one.pop())
            # 다른 극일 때를 연쇄적으로 체크(연결되어 있음)
            if check_box[0] == 0:
                two.append(two.popleft())
                if check_box[1] == 0:
                    three.appendleft(three.pop())
                    if check_box[2] == 0:
                        four.append(four.popleft())
        else:
            one.append(one.popleft())
            if check_box[0] == 0:
                two.appendleft(two.pop())
                if check_box[1] == 0:
                    three.append(three.popleft())
                    if check_box[2] == 0:
                        four.appendleft(four.pop())
    elif spin[i][0] == 2:
        if spin[i][1] == 1:
            two.appendleft(two.pop())
            # 1번째 톱니바퀴를 체크
            if check_box[0] == 0:
                one.append(one.popleft())
            # 3번째, 4번째 톱니바퀴를 체크
            if check_box[1] == 0:
                three.append(three.popleft())
                if check_box[2] == 0:
                    four.appendleft(four.pop())
        else:
            two.append(two.popleft())
            if check_box[0] == 0:
                one.appendleft(one.pop())
            if check_box[1] == 0:
                three.appendleft(three.pop())
                if check_box[2] == 0:
                    four.append(four.popleft())
    elif spin[i][0] == 3:
        if spin[i][1] == 1:
            three.appendleft(three.pop())
            # 4번째 톱니바퀴를 체크
            if check_box[2] == 0:
                four.append(four.popleft())
            # 2번째, 1번째 톱니바퀴를 체크
            if check_box[1] == 0:
                two.append(two.popleft())
                if check_box[0] == 0:
                    one.appendleft(one.pop())
        else:
            three.append(three.popleft())
            # 4번째 톱니바퀴를 체크
            if check_box[2] == 0:
                four.appendleft(four.pop())
            # 2번째, 1번째 톱니바퀴를 체크
            if check_box[1] == 0:
                two.appendleft(two.pop())
                if check_box[0] == 0:
                    one.append(one.popleft())
    if spin[i][0] == 4:
        if spin[i][1] == 1:
            four.appendleft(four.pop())
            # 다른 극일 때를 연쇄적으로 체크(연결되어 있음)
            if check_box[2] == 0:
                three.append(three.popleft())
                if check_box[1] == 0:
                    two.appendleft(two.pop())
                    if check_box[0] == 0:
                        one.append(one.popleft())
        else:
            four.append(four.popleft())
            if check_box[2] == 0:
                three.appendleft(three.pop())
                if check_box[1] == 0:
                    two.append(two.popleft())
                    if check_box[0] == 0:
                        one.appendleft(one.pop())


score = 0

if one[0] == 1:
    score += 1
if two[0] == 1:
    score += 2
if three[0] == 1:
    score += 4
if four[0] == 1:
    score += 8

print(score)
