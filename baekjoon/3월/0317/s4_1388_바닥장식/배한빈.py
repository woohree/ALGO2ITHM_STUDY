import sys
sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())

# 행의 끝에 '#' 그리고 열의 끝에 '#'로 이루어진 행을 하나 더 추가 했습니다.
deco = [sys.stdin.readline().rstrip() + '#' for _ in range(N)] + ['#' * (M+1)]

count = 0

# for문 두 번 돌리자
# '-' 찾기, row만 비교
for i in range(N):
    for j in range(M):
        # '-'만나면 다음 값 비교
        if deco[i][j] == '-':
            # 다음 값이 같은 '-'일 경우
            # --|---
            if deco[i][j + 1] == '-':
                # j + 1이 M - 1과 같다면 행의 마지막 값이라는 의미이므로 무조건 카운트
                if j + 1 == M - 1:
                    count += 1
                    break
            # 다음 값이 '|'일 경우, '-'가 끊겼으므로 카운트
            else:
                count += 1
        # '|'인 경우에서는 마지막 값이 '-'이고, 그 전 값이 '|'인 경우만 따로 계산
        # ----|-
        else:
            if j + 1 == M - 1 and deco[i][j + 1] == '-':
                count += 1
                break

# 위의 for문과 같은 맥락
# '|' 찾기, col만 비교
for m in range(M):
    for n in range(N):
        if deco[n][m] == '|':
            if deco[n + 1][m] == '|':
                if n + 1 == N:
                    count += 1
            else:
                count += 1
        else:
            if n + 1 == N and deco[n + 1][m] == '|':
                count += 1

print(count)
