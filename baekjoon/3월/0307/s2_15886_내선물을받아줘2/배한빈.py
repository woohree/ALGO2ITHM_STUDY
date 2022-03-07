# 1 × N 크기의 직사각형 지도
# E면 오른쪽, W면 왼쪽으로 한칸 이동
# 최소 몇 개의 칸 위에 선물을 놓으면, 구사과가 항상 선물을 가져가는지

# 100분
# 한시간만에 문제 제대로 이해함. 두 번째 줄이 구사과의 이동경로인줄...
# 지도 위에 알파벳들이 적혀있어 시키는대로 가야함

# 어디 위치든 E,W 시키는 대로 간 곳을 체크하는 list를 만들어야겠다.

import sys
sys.stdin = open('B.txt')

N = int(input())
directions = list(input())

# 길이가 N인 0을 가지는 list
# for문을 돌며 지나간 길은 1을 더해줄 것임.
jido = [0] * N

answer = 0
for i in range(N):
    # 0이 아닌 곳은 이미 지나간 곳이므로 0 때만 찾는다.
    if jido[i] == 0:
        # for 문이 0부터 오름차순 이므로 E가 중심이 된다는 느낌이 온다.
        if directions[i] == 'E':
            # 지나간 곳 1 더해줌
            jido[i] += 1
            # 지금 위치보다 다음의 위치에 W가 오는 것을 체크할 것이므로, 다음과 같은 조건 설정
            if i + 1 < N and directions[i+1] == 'W':
                # W를 만나면 일단 answer 카운트!
                answer += 1
                # 또 그 다음의 위치들이 W가 계속 나오면 1을 더해줘서 체크한다.
                # W면 뒤에 확인할 필요 없이 어차피 지나간 길이 겹치기 때문이다.
                while i + 1 < N and directions[i+1] == 'W':
                    jido[i+1] += 1
            # 마지막이 E일 때는 무조건 answer 카운트!
            # 반대로 첫 번째가 W일 때는 무조건 answer 카운트!
            elif i == N - 1:
                answer += 1
        # i번째가 W일 때
        # 사실 처음부터 W가 나올 경우만 해당된다.
        # 왜냐하면 아래 while문 돌면서 W가 연속해서 나오면 다 체크해 버릴 것이기 때문
        else:
            jido[i] += 1
            if i + 1 < N and directions[i+1] == 'W':
                answer += 1
                while i + 1 < N and directions[i+1] == 'W':
                    jido[i+1] += 1
                    i += 1
            # 첫 번째가 W일 때는 무조건 answer 카운트!
            elif directions[i+1] == 'E':
                answer += 1
print(answer)
