import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = list(input().rstrip())

answer = 0
cnt = 0
i = 0

while i < M - 2:
    if S[i] == "I" and S[i+1] == "O" and S[i+2] == "I": # IOI가 탐색될때마다 cnt += 1
        cnt += 1

        if cnt == N: #OI를 원하는 갯수만큼 찾았으면
            cnt -= 1  #cnt를 초기화해서 겹친 상황에서(다음에도 나오는 경우) 정상 탐색되도록 함
             answer += 1
        i += 1

    else:
        cnt = 0 #카운트 초기화
    i += 1

print(answer)