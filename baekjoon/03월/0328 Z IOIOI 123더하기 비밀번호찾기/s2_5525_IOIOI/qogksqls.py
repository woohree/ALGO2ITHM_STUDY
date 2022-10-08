# 1. slice 이용해서 풀이: 50점
# 2. slice 를 풀어서 while 두 번 돌려서 풀이: 50점
# 3. 'IOI'가 반복되는 횟수 체크

# 50분

import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())  # PN, 다른 말로 'o'의 개수
M = int(sys.stdin.readline().rstrip())  # S의 길이
S = sys.stdin.readline().rstrip()

# IOIOI
# OOIOIOIOIIOII

n = 2 * N + 1
count = answer = 0
i = 0
while i < M-2:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':  # 'IOI'
        count += 1
        # 'IOI'가 N번 만큼 반복되서 나온 경우, answer 카운트
        if count == N:
            answer += 1
            count -= 1
        i += 2
    else:
        count = 0
        i += 1

print(answer)
