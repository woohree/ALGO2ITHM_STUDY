import sys
sys.stdin = open('M.txt')


def get_point():
    now = []
    total = 0

    for task in tasks:
        # 새로운 과제가 생겼을 때, 점수와 소요시간만 append
        if task[0]:
            now.append([task[1], task[2]])

        # 해야할 과제가 있을 때 for문이 한 번 돌 때마다 마지막 과제의 시간을 1 줄여줌
        if now:
            now[-1][1] -= 1

            # 가장 최근의 과제가 끝났을 때
            if now[-1][1] == 0:
                total += now[-1][0]
                now.pop()

    return total


# 이번 학기 분
N = int(input())

tasks = [list(map(int, input().split())) for _ in range(N)]

print(get_point())
