from collections import deque

# BFS 이용
N = int(input())
hp = list(map(int, input().split()))

# SCV 한마리면 그냥 쳐서 삭제
if N == 1:
    if hp[0] >= 9 and hp[0] % 9 == 0:
        print(hp[0]//9)
    elif hp[0] < 9:
        print(1)
    else:
        print((hp[0]//9)+1)
else:
    # SCV 2마리인 경우
    if N == 2:
        queue = deque()
        queue.append([[hp[0], hp[1]], 0])
        while queue:
            next = queue.popleft()
            # 양 SCV 둘 다 피 떨어지면 break
            if next[0][0] <= 0 and next[0][1] <= 0:
                print(next[1])
                break
            # 두 가지 경우(A번 SCV를 먼저 때릴지, B번 SCV를 먼저 때릴 지를 모두 queue에 넣기)
            A = [[next[0][0]-9, next[0][1]-3], next[1]+1]
            B = [[next[0][0]-3, next[0][1]-9], next[1]+1]
            # 중복 제거로 시간 빠르게
            if A not in queue:
                queue.append(A)
            if B not in queue:
                queue.append(B)

    else:
        # SCV 3마리인 경우
        queue = deque()
        queue.append([[hp[0], hp[1], hp[2]], 0])
        while queue:
            next = queue.popleft()
            if next[0][0] <= 0 and next[0][1] <= 0 and next[0][2] <= 0:
                print(next[1])
                break
            # 6가지 경우를 모두 고려
            A = [[next[0][0]-9, next[0][1]-3, next[0][2]-1], next[1]+1]
            B = [[next[0][0]-9, next[0][1]-1, next[0][2]-3], next[1]+1]
            C = [[next[0][0]-3, next[0][1]-9, next[0][2]-1], next[1]+1]
            D = [[next[0][0]-3, next[0][1]-1, next[0][2]-9], next[1]+1]
            E = [[next[0][0]-1, next[0][1]-3, next[0][2]-9], next[1]+1]
            F = [[next[0][0]-1, next[0][1]-9, next[0][2]-3], next[1]+1]
            # 중복 제거로 시간 빠르게
            if A not in queue:
                queue.append(A)
            if B not in queue:
                queue.append(B)
            if C not in queue:
                queue.append(C)
            if D not in queue:
                queue.append(D)
            if E not in queue:
                queue.append(E)
            if F not in queue:
                queue.append(F)