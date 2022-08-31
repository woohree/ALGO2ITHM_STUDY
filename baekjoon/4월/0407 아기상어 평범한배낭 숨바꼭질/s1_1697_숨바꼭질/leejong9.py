import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def finding(n,s):
    if visited[n] == 0 or visited[n] > s: #방문한 적이 없거나 기존 방문기록보다 짧은 시간만에 방문했다면
        visited[n] = s #새로운 기록을 남긴다
        if n > 0 and n < 2 * K - 1:
            finding(n * 2, s + 1)
            finding(n + 1, s + 1)
            finding(n - 1, s + 1)






N, K = map(int,input().split())

visited = [0]*4*K
finding(N,0) #현재 위치에서 시작
print(visited[K]) #동생 위치에서의 최고기록을 출력


