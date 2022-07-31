import sys, bisect
sys.stdin = open('W.txt')


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
sum_A, sum_B = [], []                           # 각각 모든 부분합
for i in range(n):
    a = 0
    for j in range(i, n):
        a += A[j]
        sum_A.append(a)
for i in range(m):
    b = 0
    for j in range(i, m):
        b += B[j]
        sum_B.append(b)
ans = 0
# for sum_a in sum_A:                             # 외않돼...
#     ans += sum_B.count(T-sum_a)                 # count는 개느린 거시다...
sum_A.sort()
sum_B.sort()
for sum_a in sum_A:                             # bisect를 쓰면 정렬된 배열에서, 동일한 값의 왼쪽 오른쪽 인덱스를 찾을 수 있음
    l = bisect.bisect_left(sum_B, T-sum_a)
    r = bisect.bisect_right(sum_B, T-sum_a)
    ans += r - l                                # 인덱스 차이 = 가능한 부분합 갯수
print(ans)