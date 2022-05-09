import sys
sys.stdin = open('M.txt')

R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]

temp = ['' for _ in range(C)]       # 문자열 저장용
ans = R - 1
for i in range(R - 1, 0, -1):       # 마지막 행부터 탐색
    for j in range(C):
        temp[j] += arr[i][j]
    if len(set(temp)) == C:         # 중복되는 문자열이 없어졌을 때
        break
    ans -= 1

print(ans)
