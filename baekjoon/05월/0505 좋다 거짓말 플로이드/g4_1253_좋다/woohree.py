import sys
sys.stdin = open('L.txt')


# PyPy로 6056ms ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
cnt = 0
for i in range(N):                          # i => Good인지 확인할 수
    for j in range(N):                      # j => 왼쪽(작은 수)부터 확인
        if j != i:
            trigger = 0
            for k in range(N-1, j, -1):     # k => 오른쪽(큰 수)부터 확인
                if k not in (i, j) and numbers[j] + numbers[k] <= numbers[i]:
                    if numbers[j] + numbers[k] == numbers[i]:  # j번 + k번이 i번이 되면 cnt +1 하고 break
                        cnt += 1
                        trigger = 1
                    break
            if trigger:
                break
print(cnt)