import sys
sys.stdin = open('G.txt')


def solution(N):
    times = [list(map(int, input().split())) for _ in range(N)]

    # 종료시간을 기준으로 오름차순
    times.sort(key=lambda x: (x[1], x[0]))

    meeting_cnt = 0
    last_time = 0

    for time in times:
        # 현재 회의의 시작시간이 마지막 종료시간 보다 크거나 같다면
        if time[0] >= last_time:
            # 종료시간을 현재 회의의 종료시간으로
            last_time = time[1]
            meeting_cnt += 1
    
    return meeting_cnt


N = int(input())
answer = solution(N)
print(answer)