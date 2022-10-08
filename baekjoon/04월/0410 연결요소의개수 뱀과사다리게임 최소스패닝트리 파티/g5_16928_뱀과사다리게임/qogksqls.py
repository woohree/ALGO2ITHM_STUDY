# 40m
import sys
sys.stdin = open('B.txt')

from collections import deque

# bfs 로 풀이
# 88ms


def bfs():
    global count

    while current:
        for _ in range(len(current)):
            temp = current.popleft()
            for i in range(6, 0, -1):
                next = temp + i
                if next <= 100 and visited[next] == 0:
                    visited[next] = 1
                    # next 값이 사다리 시작 위치에 있을 경우
                    if next in ladder_s:
                        for l in ladders:
                            if l[0] == next:
                                current.append(l[1])
                                break
                    # next 값이 뱀 시작 위치에 있을 경우
                    elif next in snake_s:
                        for s in snakes:
                            if s[0] == next:
                                current.append(s[1])
                                break
                    # next 값이 사다리와 뱀 시작 위치에 없을 경우
                    else:
                        current.append(next)
        count += 1
        if 100 in current:
            return


N, M = map(int, sys.stdin.readline().rstrip().split())
ladders = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
snakes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

# 사다리와 뱀의 시작위치만 저장하는 리스트
ladder_s = []
for ladder in ladders:
    ladder_s.append(ladder[0])
snake_s = []
for snake in snakes:
    snake_s.append(snake[0])

visited = [0, 1] + [0] * 99
current = deque([1])
count = 0
bfs()

print(count)

'''
# 1등 풀이, 56ms
# 다른 점: list 말고 dict 를 이용해서 품
#         stack 썼는데 이건 deque 을 아직 안 배운 분인가 싶었음
def solution(SL):
    visited=[1]
    stack=[1]
    answer=0
    while 1:
        t_stack=[]
        while stack:
            s=stack.pop()
            for k in range(1,7):
                temp=k+s
                if temp not in visited:
                    if temp in SL:
                        visited.append(temp)
                        visited.append(SL[temp])
                        t_stack.append(SL[temp])
                    else:
                        visited.append(temp)
                        t_stack.append(temp)
        stack=t_stack
        answer+=1
        if 100 in visited:
            break
    return answer
            
n=input()
n=n.split()
SL={}
for i in range(int(n[0])+int(n[1])):
    s = list(map(int, input().split()))
    SL[s[0]]=s[1]
print(solution(SL))
'''