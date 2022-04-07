# 백준 1026 보물 S4 문제
# 2:00 시작 2:10 성공 => 10분 소요

import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# sort 함수 안쓰고 구함
for i in range(N):
    for j in range(len(A)-1):  # 밑에 j+1을 써야하므로 여기선 range에선 1을 뺀 값을 사용. 안쓰면 범위를 벗어난 계산이 됨
        if A[j] > A[j+1]:  # A를 오름차순 정렬. A[j]가 A[j+1]보다 클때는 j가 3인 순간.
            temp = A[j]  # A가 [1, 1, 1, 6, 0]이고 j=3일때, temp=6
            A[j] = A[j+1]  # A[3]=0이 되고
            A[j+1] = temp  # A[4]=6이 되면서 큰 값이 뒤로 감.

for i in range(N):
    for j in range(len(B)-1):
        if B[j] < B[j+1]:  # B를 내림차순 정렬
            temp = B[j]
            B[j] = B[j+1]
            B[j+1] = temp

S = 0
for i in range(N):
    S += A[i] * B[i]  # S에 A, B의 i번째 순서대로 곱한걸 더함

print(S)


# sort 함수를 써서 구함
# A.sort(reverse = True)
# B.sort()
#
# S = 0
# for i in range(N):
#     S += A[i] * B[i]