# 길이가 n인 정수
# 정수 배열 A와 B
# 함수 S = A[0] * B[0] + ... + A[N-1] * B[N-1]
# S의 값을 가장 작게 만들기 위해서 A의 수 재배열
# S의 최솟값을 출력

import sys
sys.stdin = open('input.txt')

# B의 큰 수의 위치에 A의 작은 수부터


# sort 사용
def func_s():
    A.sort()
    B.sort(reverse=True)

    s = 0

    for i in range(N):
        s += A[i] * B[i]
    
    print(s)


# sort 사용 x
def func():

    # 재배열 여부 확인용
    temp = [0] * N

    for i in range(N):

        max_idx = min_idx = 0

        # 재배열 되지 않은 가장 첫 번째 요소로 초기화
        for idx in range(N):
            if temp[idx] == 0:
                min_val = A[idx]
                max_val = B[idx]
                break

        for j in range(N):

            # 이미 재배열 된 값이 있으면
            if temp[j] == 1:
                continue

            if B[j] >= max_val:
                max_val = B[j]
                max_idx = j

            if A[j] <= min_val:
                min_val = A[j]
                min_idx = j

        # A 재배열
        A[max_idx], A[min_idx] = A[min_idx], A[max_idx]

        temp[max_idx] = 1

    s = 0

    for i in range(N):
        s += A[i] * B[i]

    print(s)


T = int(input())

for tc in range(T):
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    func()
