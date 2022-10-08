import sys
sys.stdin = open('M.txt')

N = int(input())
A = list(map(int, input().split()))

ans = 0
dic_a = dict()              # 가능한 모든 조합의 합 key, 조합 인덱스 리스트 value
for i in range(N - 1):
    for j in range(i + 1, N):
        dic_a.setdefault(A[i] + A[j], []).append((i, j))

for idx in range(N):
    if dic_a.get(A[idx]):   # 각 숫자가 두 숫자의 합이 될 수 있을 때
        for key in dic_a[A[idx]]:
            if idx not in key:      # 자신이 포함되지 않으면
                ans += 1
                break

print(ans)
