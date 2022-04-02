import sys
sys.stdin = open('G.txt')

def get_time(N):
    times = list(map(int, input().split()))

    times.sort()

    # 정렬된후 각 사람이 기다린 시간으로 리스트 원소 변경
    for i in range(1, N):
        times[i] = times[i] + times[i-1]

    return sum(times)

N = int(input())
answer = get_time(N)
print(answer)
