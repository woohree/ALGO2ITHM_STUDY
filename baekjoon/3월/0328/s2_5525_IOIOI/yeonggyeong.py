import sys
sys.stdin = open('G.txt')

N = int(input())
M = int(input())
string = input()

# N = 1 -> IOI
# N = 2 -> IOIOI -> IOI가 2개
# N = 3 -> IOIOIOI -> IOI가 3개
answer = 0
cnt = 0
i = 0
while i < M-1:
    # 연속된 세 문자
    if string[i:i+3] == 'IOI':
        # 'IOI'의 카운트
        cnt += 1
        # 연속된 IOI의 개수가 N과 같다면 Pn이 존재한다는 것 
        if cnt == N:
            cnt -= 1
            answer += 1
        
        i += 1
    else:
        cnt = 0
    i += 1


print(answer)