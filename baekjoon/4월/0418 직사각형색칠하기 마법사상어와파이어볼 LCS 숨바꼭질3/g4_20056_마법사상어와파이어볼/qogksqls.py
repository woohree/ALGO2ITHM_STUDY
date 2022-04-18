import sys
sys.stdin = open('B.txt')

N, M, K = map(int, sys.stdin.readline().rstrip().split())  # 행렬 크기, 파이어볼 개수, 명령 횟수
fireballs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]  # 행, 열, 질량, 속력, 방향

# 파이어볼 좌상단이 (1, 1)부터 시작이므로 좌표 값들을 1씩 빼고 시작
for n in range(M):
    fireballs[n][0] -= 1
    fireballs[n][1] -= 1

directions = {
    0: [-1, 0],
    1: [-1, 1],
    2: [0, 1],
    3: [1, 1],
    4: [1, 0],
    5: [1, -1],
    6: [0, -1],
    7: [-1, -1],
}

# K번 돌기
while K != 0:
    memories = [[0] * N for _ in range(N)]  # [질량, 속력, 방향(홀짝), 개수, 방향] 의 list 를 입력할 것임!
    for f in range(len(fireballs)):
        # 알맞는 방향과 속력으로 파이어볼의 좌표 이동
        fireballs[f][0] += directions[fireballs[f][4]][0] * fireballs[f][3]
        fireballs[f][1] += directions[fireballs[f][4]][1] * fireballs[f][3]

        # 파이어볼의 좌표가 음수가 되거나 N을 넘어간 경우에 N의 나머지로 출력
        if fireballs[f][0] < 0 or fireballs[f][0] >= N:
            fireballs[f][0] %= N
        if fireballs[f][1] < 0 or fireballs[f][1] >= N:
            fireballs[f][1] %= N

        # memories에 0이 아닌 리스트가 있을 경우
        if memories[fireballs[f][0]][fireballs[f][1]]:
            # 질량과 속력은 값을 누적시키고, 개수는 +1 해준다.
            memories[fireballs[f][0]][fireballs[f][1]][0] += fireballs[f][2]
            memories[fireballs[f][0]][fireballs[f][1]][1] += fireballs[f][3]
            memories[fireballs[f][0]][fireballs[f][1]][3] += 1

            # 방향이 기존에 저장되있던 값(홀수,짝수)과 다를 경우 2로 바꾼다.
            if memories[fireballs[f][0]][fireballs[f][1]][2] != 2:
                if fireballs[f][4] % 2 != memories[fireballs[f][0]][fireballs[f][1]][2]:
                    memories[fireballs[f][0]][fireballs[f][1]][2] = 2

        # memories의 파이어볼 좌표가 값이 0인 경우
        else:
            # 홀수, 짝수 두 가지 경우로 나누어 리스트 저장 => [질량, 속력, 방향(홀짝), 개수, 방향]
            if fireballs[f][4] % 2:
                memories[fireballs[f][0]][fireballs[f][1]] = [fireballs[f][2], fireballs[f][3], 1, 1, fireballs[f][4]]
            else:
                memories[fireballs[f][0]][fireballs[f][1]] = [fireballs[f][2], fireballs[f][3], 0, 1, fireballs[f][4]]

    temp = []
    for i in range(N):
        for j in range(N):
            if memories[i][j]:
                if memories[i][j][3] > 1:
                    if memories[i][j][0] // 5 > 0:
                        if memories[i][j][2] == 2:
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 1])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 3])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 5])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 7])
                        else:
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 0])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 2])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 4])
                            temp.append([i, j, memories[i][j][0] // 5, memories[i][j][1] // memories[i][j][3], 6])
                else:
                    temp.append([i, j, memories[i][j][0], memories[i][j][1], memories[i][j][4]])
    fireballs = temp[:]
    K -= 1

answer = 0
for fireball in fireballs:
    answer += fireball[2]
print(answer)
