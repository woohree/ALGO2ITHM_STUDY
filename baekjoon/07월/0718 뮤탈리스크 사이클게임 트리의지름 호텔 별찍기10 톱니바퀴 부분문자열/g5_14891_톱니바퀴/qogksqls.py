import sys
sys.stdin = open('B.txt')

'''
60분
1. 톱니의 2, 6번 이빨만 따로 info 리스트에 저장.
2. 3단계로 나뉨
    1. 해당 톱니 무조건 회전
    2. 오른쪽 톱니 회전
    3. 왼쪽 톱니 회전
3. 인덱스 잘못 설정해서 시간 겁나 날림..
'''

cogwheels = [list(sys.stdin.readline().rstrip()) for _ in range(4)]
K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    num, d = map(int, sys.stdin.readline().rstrip().split())
    num -= 1
    info = [  # 1번
        [cogwheels[0][2], cogwheels[0][6]],
        [cogwheels[1][2], cogwheels[1][6]],
        [cogwheels[2][2], cogwheels[2][6]],
        [cogwheels[3][2], cogwheels[3][6]],
    ]

    # 현재 톱니 우선 회전
    temp = []
    if d == -1:
        for j in range(1, 8):
            temp.append(cogwheels[num][j])
        temp.append(cogwheels[num][0])
    else:
        temp.append(cogwheels[num][-1])
        for j in range(7):
            temp.append(cogwheels[num][j])
    cogwheels[num] = temp[:]

    # 오른쪽 톱니들 회전
    copy_d = d
    for i in range(num, 3):
        if info[i][0] != info[i+1][1]:
            temp = []
            if copy_d == 1:
                for j in range(1, 8):
                    temp.append(cogwheels[i+1][j])
                temp.append(cogwheels[i+1][0])
                copy_d -= 2
            else:
                temp.append(cogwheels[i+1][-1])
                for j in range(7):
                    temp.append(cogwheels[i+1][j])
                copy_d += 2
            cogwheels[i+1] = temp[:]
        else:
            break

    # 왼쪽 톱니들 회전
    for i in range(num, 0, -1):
        if info[i][1] != info[i-1][0]:
            temp = []
            if d == 1:
                for j in range(1, 8):
                    temp.append(cogwheels[i-1][j])
                temp.append(cogwheels[i-1][0])
                d -= 2
            else:
                temp.append(cogwheels[i-1][-1])
                for j in range(7):
                    temp.append(cogwheels[i-1][j])
                d += 2
            cogwheels[i-1] = temp[:]
        else:
            break

ans = 0
for i in range(4):
    if cogwheels[i][0] == '1':
        ans += 2 ** i
print(ans)
