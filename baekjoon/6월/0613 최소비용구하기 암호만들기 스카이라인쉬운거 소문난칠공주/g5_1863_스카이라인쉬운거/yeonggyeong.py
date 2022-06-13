import sys
sys.stdin = open('G.txt')

n = int(sys.stdin.readline())

stack = []
buildings = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 전 입력보다 현재 입력의 y좌표가 작을 경우 -> building +1 / 클 때까지 pop 해주기
    while stack and stack[-1] > y:
        buildings += 1
        stack.pop()
        
    # 크기가 같다면 넘어가기
    if stack and stack[-1] == y:
        continue
    stack.append(y)

buildings += len(stack)

if 0 in stack:
    buildings -= 1
print(buildings)