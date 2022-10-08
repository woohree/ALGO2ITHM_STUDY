import sys
sys.stdin = open('B.txt')

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()


# T에서 제거하는 방법
def solution(T):
    global flag
    if T == S:
        flag = 1
        return
    l = len(T)
    if len(S) == l:
        return
    if T[l-1] == 'A':
        solution(T[:l-1])
        if flag:
            return
    if T[0] == 'B':
        solution(T[1:l][::-1])
        if flag:
            return


flag = 0
solution(T)
print(flag)

'''dfs
def dfs(S):
    global flag
    if S == T:
        flag = 1
        return
    if len(S) == len(T):
        return
    dfs(S+'A')
    if flag:
        return
    dfs((S+'B')[::-1])
    if flag:
        return


flag = 0
dfs(S)
if flag: print(1)
else: print(0)
'''

''' 메모리초과
from collections import deque

def bfs():
    q = deque()
    q.append(S)
    while q:
        now = q.popleft()
        if len(now) == len(T):
            return 0
        next_1 = now + 'A'
        next_2 = (now + 'B')[::-1]
        if next_1 == T or next_2 == T:
            return 1
        q.append(next_1)
        q.append(next_2)
'''