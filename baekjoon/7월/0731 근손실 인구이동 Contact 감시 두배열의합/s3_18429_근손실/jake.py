import sys
sys.stdin = open('input.txt')

def DFS(days, strength, kit):
    global check
    global answer
    if strength<500:
        return
    if days == N and strength >= 500:
        answer += 1
        return
    for j in range(N):
        if check[j] == 0:
            check[j] = 1
            DFS(days+1, strength-K+A[j], A[j])
            check[j] = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))
answer = 0
for i in range(N):
    check = [0]*N
    check[i] = 1
    DFS(1, 500-K+A[i], A[i])
print(answer)